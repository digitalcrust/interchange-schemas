# tests/test_converter.py
import json
from pathlib import Path

import pytest

from digitalcrust.interchange_schemas.converter import (
    multiple_spots_to_fieldsites,
    checkin_to_fieldsite,
    fieldsite_to_spot,
    fieldsite_to_checkin,
)
from digitalcrust.interchange_schemas.field_site import FieldSite, PlanarOrientation


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SPOT_PATH = ROOT / "test-data/strabospot/complete-spot.json"
DEFAULT_CHECKIN_PATH = ROOT / "test-data/rockd/checkin-26692.json"


def _to_mapping(obj):
    """Turn Pydantic v1/v2 models into plain dicts for printing."""
    md = getattr(obj, "model_dump", None)   # pydantic v2
    if callable(md):
        try:
            return md(mode="json")
        except TypeError:
            return md()
    dct = getattr(obj, "dict", None)        # pydantic v1
    if callable(dct):
        return dct()
    return obj


def _read_json(path: Path):
    with path.open() as f:
        return json.load(f)

def pytest_addoption(parser):
    parser.addoption("--spot", action="store", help="Path to StraboSpot JSON")
    parser.addoption("--checkin", action="store", help="Path to Rockd checkin JSON")

@pytest.fixture(scope="session")
def spot_json(request):
    path = request.config.getoption("--spot") or DEFAULT_SPOT_PATH
    return _read_json(Path(path))

@pytest.fixture(scope="session")
def checkin_json(request):
    path = request.config.getoption("--checkin") or DEFAULT_CHECKIN_PATH
    return _read_json(Path(path))






# Spot -> FieldSite
def test_spot_to_fieldsite_to_checkin(spot_json):
    fs_list = multiple_spots_to_fieldsites(spot_json)
    assert isinstance(fs_list, list)
    assert fs_list, "No valid spot found."
    fs = fs_list[0]
    assert isinstance(fs, FieldSite)
    print("\n=== FieldSite (from Spot) ===")
    print(json.dumps(_to_mapping(fs), indent=2, default=str))

    #basic required fields
    assert fs.id is not None
    assert fs.location is not None
    assert isinstance(fs.location.latitude, float)
    assert isinstance(fs.location.longitude, float)
    assert fs.created is not None
    assert fs.updated is not None

    if fs.observations:
        planars = [
            ob.data for ob in fs.observations
            if isinstance(getattr(ob, "data", None), PlanarOrientation)
        ]
        if planars:
            po = planars[0]
            assert isinstance(po.strike, (int, float))
            assert isinstance(po.dip, (int, float))

    #FieldSite -> Rockd checkin
    chk = fieldsite_to_checkin(fs)
    print("\n=== Checkin (from FieldSite and Spot) ===")
    print(json.dumps(chk, indent=2))
    assert isinstance(chk, dict)
    for key in ("checkin_id", "lat", "lng", "created"):
        assert key in chk
    if fs.observations and any(isinstance(ob.data, PlanarOrientation) for ob in fs.observations):
        assert "observations" in chk
        assert isinstance(chk["observations"], list)
        assert chk["observations"], "observations list should not be empty"
        ori0 = chk["observations"][0].get("orientation", {})
        assert "strike" in ori0 and "dip" in ori0

#---------------------------------------------------------------------------------
# Checkin -> FieldSite
def test_checkin_to_fieldsite_to_spot(checkin_json):
    # 1) Rockd checkin -> FieldSite
    fs = checkin_to_fieldsite(checkin_json)
    assert isinstance(fs, FieldSite)
    print("\n=== FieldSite (from Checkin) ===")
    print(json.dumps(_to_mapping(fs), indent=2, default=str))
    # Basic required fields
    assert fs.id is not None
    assert fs.location is not None
    assert isinstance(fs.location.latitude, float)
    assert isinstance(fs.location.longitude, float)
    assert fs.created is not None
    assert fs.updated is not None

    had_planar = False
    if isinstance(checkin_json.get("observations"), list):
        for o in checkin_json["observations"]:
            ori = (o or {}).get("orientation") or {}
            if "strike" in ori and "dip" in ori:
                had_planar = True
                break

    if had_planar:
        assert fs.observations, "Expected planar observation to be carried into FieldSite"
        assert any(isinstance(ob.data, PlanarOrientation) for ob in fs.observations)

    # FieldSite -> Spot
    spot_fc = fieldsite_to_spot(fs)

    print("\n=== Spot (from FieldSite and checkin) ===")
    print(json.dumps(spot_fc, indent=2))
    assert isinstance(spot_fc, dict)
    assert spot_fc.get("type") == "FeatureCollection"
    feats = spot_fc.get("features")
    assert isinstance(feats, list) and feats
    feat0 = feats[0]
    assert feat0.get("type") == "Feature"
    assert feat0.get("geometry", {}).get("type") == "Point"
    props = feat0.get("properties", {})
    for key in ("id", "lat", "lng", "time"):
        assert key in props

    if fs.observations and any(isinstance(ob.data, PlanarOrientation) for ob in fs.observations):
        assert "orientation_data" in props
        assert isinstance(props["orientation_data"], list)
        assert props["orientation_data"], "orientation_data list should not be empty"
        od0 = props["orientation_data"][0]
        assert od0.get("type") == "planar_orientation"
        assert "strike" in od0 and "dip" in od0
