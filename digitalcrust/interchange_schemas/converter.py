from datetime import datetime, timezone
from .field_site import FieldSite, Location, Photo, PlanarOrientation, Observation, BeddingFacing
from typing import Optional
import json, sys


# ---- Minimal field mapping (intersection only) ----
# ID: Spot properties.id ↔ Checkin checkin_id → FieldSite.id
# Notes: Spot properties.notes ↔ Checkin notes → FieldSite.notes
# When: Spot properties.time || date ↔ Checkin created → FieldSite.created
#       (Spot modified_timestamp ↔ Checkin added → FieldSite.updated)
# Location: Spot properties.lat/lng (or Point geometry) ↔ Checkin lat/lng → FieldSite.location
# Photo: Spot properties.images[0].id ↔ Checkin photo → FieldSite.photos[0].id
# (Name and Social intentionally excluded — not shared)


#------------Helpers---------------
#normalize date/times.
def _parse_date_time(x: Optional[str]) -> Optional[datetime]:
    if not x:
        return None
    try:
        return datetime.fromisoformat(x.replace("Z", "+00:00"))
    except Exception:
        try:
            return datetime.strptime(x, "%B %d, %Y").replace(tzinfo=timezone.utc)
        except Exception:
            return None

def _to_float(v) -> Optional[float]:
    try:
        if v is None:
            return None
        return float(v)
    except Exception:
        return None

#normalize and require lat/lngs
def _valid_coords(lat, lng) -> bool:
    try:
        lat = float(lat)
        lng = float(lng)
    except (TypeError, ValueError):
        return False
    return -90.0 <= lat <= 90.0 and -180.0 <= lng <= 180.0

def _first_planar_from_spot(props) -> Optional[PlanarOrientation]:
    """Find first planar orientation with numeric strike & dip in StraboSpot props."""
    orientation = props.get("orientation_data")
    if not isinstance(orientation, list):
        return None
    for item in orientation:
        if not isinstance(item, dict):
            continue
        if item.get("type") == "planar_orientation":
            strike = _to_float(item.get("strike"))
            dip = _to_float(item.get("dip"))
            if strike is not None and dip is not None:
                return PlanarOrientation(strike=strike, dip=dip, facing=BeddingFacing.upright)
    return None

def _first_planar_from_checkin(checkin) -> Optional[PlanarOrientation]:
    """Find first observation with numeric strike & dip in Rockd checkin."""
    obs = checkin.get("observations")
    if not isinstance(obs, list):
        return None
    for o in obs:
        if not isinstance(o, dict):
            continue
        orientation = o.get("orientation") or {}
        strike = _to_float(orientation.get("strike"))
        dip = _to_float(orientation.get("dip"))
        if strike is not None and dip is not None:
            return PlanarOrientation(strike=strike, dip=dip, facing=BeddingFacing.upright)
    return None

def _first_planar_from_fieldsite(fs: FieldSite) -> Optional[PlanarOrientation]:
    """Return first PlanarOrientation in FieldSite.observations."""
    for ob in fs.observations or []:
        data = getattr(ob, "data", None)
        if isinstance(data, PlanarOrientation):
            return data
    return None

#------------Single spot to FieldSite---------------
def spot_to_fieldsite(feat) -> FieldSite:
    props = feat.get("properties", {}) or {}
    geom = feat.get("geometry", {}) or {}
    # require id
    sid = props.get("id")
    if sid is None:
        raise ValueError("Missing spot properties.id")
    lat = props.get("lat")
    lng = props.get("lng")
    if (lat is None or lng is None) and geom.get("type") == "Point":
        coords = geom.get("coordinates", []) or []
        if len(coords) >= 2:
            lng = coords[0] if lng is None else lng
            lat = coords[1] if lat is None else lat

    if not _valid_coords(lat, lng):
        raise ValueError("Invalid or missing lat/lng for Spot feature")

    photos = []
    images = props.get("images")
    if isinstance(images, list) and images:
        img = images[0] or {}
        pid = img.get("id")
        if pid is not None:
            photos.append(
                Photo(
                    id=int(pid),
                    url=f"rockd://photo/{pid}",
                    width=int(img.get("width", 0) or 0),
                    height=int(img.get("height", 0) or 0),
                    checksum=""
                )
            )
    observations: list[Observation] = []
    planar = _first_planar_from_spot(props)
    if planar:
        observations.append(Observation(data=planar))
    created = _parse_date_time(props.get("time") or props.get("date")) or datetime.now(timezone.utc)

    mt = props.get("modified_timestamp")
    if mt is not None:
        try:
            updated = datetime.fromtimestamp(float(mt) / 1000.0, tz=timezone.utc)
        except Exception:
            updated = created
    else:
        updated = created

    return FieldSite(
        id=sid,
        location=Location(latitude=float(lat), longitude=float(lng)),
        created=created,
        updated=updated,
        notes=props.get("notes"),
        photos=photos,
        observations=observations,

    )

#------------Multiple spots to list[FieldSite]---------------
def multiple_spots_to_fieldsites(multiple_spots) -> list[FieldSite]:
    assert multiple_spots.get("type") == "FeatureCollection"
    out: list[FieldSite] = []

    for f in multiple_spots.get("features", []):
        props = f.get("properties", {}) or {}
        geom = f.get("geometry", {}) or {}

        # must have id  // added
        if props.get("id") is None:
            continue

        lat = props.get("lat")
        lng = props.get("lng")
        if lat is None or lng is None:
            if geom.get("type") == "Point":
                coords = geom.get("coordinates", []) or []
                if len(coords) < 2 or not _valid_coords(coords[1], coords[0]):
                    continue
            else:
                continue
        try:
            out.append(spot_to_fieldsite(f))
        except Exception:
            continue
    return out

#------------Single checkin to FieldSite---------------
def checkin_to_fieldsite(checkin) -> FieldSite:
    cid = checkin.get("checkin_id")
    if cid is None:
        raise ValueError("Missing checkin_id")

    lat, lng = checkin.get("lat"), checkin.get("lng")
    if not _valid_coords(lat, lng):
        raise ValueError("Invalid or missing lat/lng for Checkin")

    photos = []
    if isinstance(checkin.get("photo"), int):
        pid = checkin["photo"]
        photos.append(
            Photo(
                id=int(pid),
                url=f"rockd://photo/{pid}",
                width=0,
                height=0,
                checksum=""
            )
        )
    observations: list[Observation] = []
    planar = _first_planar_from_checkin(checkin)
    if planar:
        observations.append(Observation(data=planar))
    created = _parse_date_time(checkin.get("created")) or datetime.now(timezone.utc)
    updated = _parse_date_time(checkin.get("added")) or created

    return FieldSite(
        id=cid,
        location=Location(latitude=float(lat), longitude=float(lng)),
        created=created,
        updated=updated,
        notes=checkin.get("notes"),
        photos=photos,
        observations=observations,
    )



#------------------Fieldsite to checkin OR spot----------------------------



# ---- FieldSite to spot ----
def fieldsite_to_spot(fs: FieldSite) -> dict:
    feat = {
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [fs.location.longitude, fs.location.latitude]},
        "properties": {
            "id": fs.id,
            "notes": fs.notes,
            "time": fs.created.isoformat(),
            "lat": fs.location.latitude,
            "lng": fs.location.longitude,
        }
    }
    if fs.photos:
        feat["properties"]["images"] = [{"id": fs.photos[0].id}]

    planar = _first_planar_from_fieldsite(fs)
    if planar:
        feat["properties"]["orientation_data"] = [{
            "type": "planar_orientation",
            "strike": float(planar.strike),
            "dip": float(planar.dip)
        }]
    return {"type": "FeatureCollection", "features": [feat]}

def fieldsite_to_checkin(fs: FieldSite) -> dict:
    d = {
        "checkin_id": fs.id,
        "notes": fs.notes,
        "lat": fs.location.latitude,
        "lng": fs.location.longitude,
        "created": fs.created.isoformat(),
    }
    if fs.photos:
        d["photo"] = fs.photos[0].id
    planar = _first_planar_from_fieldsite(fs)
    if planar:
        d["observations"] = [{"orientation": {"strike": float(planar.strike), "dip": float(planar.dip)}}]

    return d



'''
if __name__ == "__main__":
    def dump(o):
        try:
            print(json.dumps(o.model_dump(), default=str, indent=2))  # Pydantic v2
        except Exception:
            try:
                print(json.dumps(o.dict(), default=str, indent=2))    # Pydantic v1
            except Exception:
                print(json.dumps(o, default=str, indent=2))

    if len(sys.argv) != 3 or sys.argv[1] not in ("spot2checkin","checkin2spot","to-spot","to-checkin"):
        sys.exit("usage: python converter.py {spot2checkin|checkin2spot|to-spot|to-checkin} path/to/input.json")

    mode, path = sys.argv[1], sys.argv[2]
    with open(path) as f:
        data = json.load(f)

    if mode == "spot2checkin":
        # 1) FeatureCollection -> FieldSite (first convertible)
        fs_list = multiple_spots_to_fieldsites(data)
        if not fs_list:
            sys.exit("no convertible spot found")
        fs = fs_list[0]
        print("\n=== FieldSite (from Spot) ===")
        dump(fs)

        # 2) FieldSite -> Checkin
        chk = fieldsite_to_checkin(fs)
        print("\n=== Checkin (from FieldSite) ===")
        dump(chk)

    elif mode == "checkin2spot":
        # 1) Checkin -> FieldSite
        fs = checkin_to_fieldsite(data)
        print("\n=== FieldSite (from Checkin) ===")
        dump(fs)

        # 2) FieldSite -> Spot (FeatureCollection)
        spot_fc = fieldsite_to_spot(fs)
        print("\n=== Spot FeatureCollection (from FieldSite) ===")
        dump(spot_fc)

    else:
        fs = FieldSite(**data)
        if mode == "to-spot":
            print("\n=== Spot FeatureCollection (from FieldSite) ===")
            dump(fieldsite_to_spot(fs))
        else:
            print("\n=== Checkin (from FieldSite) ===")
            dump(fieldsite_to_checkin(fs))
'''