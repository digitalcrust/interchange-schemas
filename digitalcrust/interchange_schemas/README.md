# FieldSite Interchange

Rockd (**checkins**) and StraboSpot (**spots**) need a **shared, minimal interchange** so that core field metadata round-trips cleanly between the two apps. This repo defines a compact Pydantic model called **`FieldSite`** and a set of **one-directional** and **bidirectional** converters that preserve **only the intersection of data** present in _both_ systems.

---

## 1) Goals & Principles

- **Single source of truth:** `FieldSite` is the neutral interchange.
- **Intersection only:** Map only fields that exist on both platforms today. This keeps the contract stable while you iterate.
- **Loss-minimized, not lossless:** We don’t attempt to carry platform-specific extras.
- **Deterministic round-trips:** Conversions should be predictable and easy to test.
- **Strict location validity:** Geographic coordinates must be real lat/lng (no image pixels).

**Required at minimum for this interchange:**
- `FieldSite.id`
- `FieldSite.location.latitude`
- `FieldSite.location.longitude`
- `FieldSite.created`
- `FieldSite.updated`
---
## Minimal Field Mapping (intersection only)

### StraboSpot ⇒ FieldSite
**Ignored fields from spot for now:** `properties.name`, `altitude`, `gps_accuracy`, non-point geometry without lat/lng, additional photos.
**Supported inputs:** a single `Feature` or a `FeatureCollection` (we convert the first convertible feature).  
**If `properties.lat/lng` are missing**, a `Point` geometry’s `[lng, lat]` is used.

|FieldSite target|StraboSpot source|Notes|
|---|---|---|
|`id`|`properties.id`|**Required**; error if missing.|
|`location.latitude`|`properties.lat` or `geometry.Point[1]`|Must be a valid lat.|
|`location.longitude`|`properties.lng` or `geometry.Point[0]`|Must be a valid lng.|
|`created`|`properties.time` or `properties.date`|ISO (supports `Z`) or `"Month DD, YYYY"`. Fallback: now(UTC).|
|`updated`|`properties.modified_timestamp` (ms epoch)|Converted to UTC; fallback: `created`.|
|`notes`|`properties.notes`|Optional.|
|`photos[0]`|`properties.images[0]`|First image only. `url` is `rockd://photo/{id}`; width/height if present; checksum `""`.|


---
### Rockd Checkin ⇒ FieldSite
**Ignored from checkin for now:** `first_name`, `last_name`, `near`, `likes`, `comments`, `rating`, `observations`, `xp`, `stats`, etc

|FieldSite target|Rockd source|Notes|
|---|---|---|
|`id`|`checkin_id`|**Required**; error if missing.|
|`location.latitude`|`lat`|Must be a valid lat.|
|`location.longitude`|`lng`|Must be a valid lng.|
|`created`|`created`|ISO (supports `Z`) or `"Month DD, YYYY"`. Fallback: now(UTC).|
|`updated`|`added`|Same parsing; fallback: `created`.|
|`notes`|`notes`|Optional.|
|`photos[0]`|`photo` (int)|First/only; `url` is `rockd://photo/{id}`; width/height `0`; checksum `""`.|


---

### FieldSite ⇒ StraboSpot (single feature FC)

Outputs a **single-feature FeatureCollection** with a **Point** geometry.

|Spot target|FieldSite source|Notes|
|---|---|---|
|`FeatureCollection.features[0]`|(constructed)|Always 1 feature.|
|`geometry.coordinates`|`location.{lng,lat}`|Point only.|
|`properties.id`|`id`|Required.|
|`properties.time`|`created.isoformat()`||
|`properties.lat / properties.lng`|`location.latitude/longitude`|Convenience duplication.|
|`properties.notes`|`notes`|Optional.|
|`properties.images[0].id`|`photos[0].id` (if any)|First photo only.|

---

### FieldSite ⇒ Rockd Checkin

| Checkin target | FieldSite source              | Notes             |
| -------------- | ----------------------------- | ----------------- |
| `checkin_id`   | `id`                          | Required.         |
| `created`      | `created.isoformat()`         |                   |
| `lat` / `lng`  | `location.latitude/longitude` | Required.         |
| `notes`        | `notes`                       | Optional.         |
| `photo`        | `photos[0].id` (if any)       | First photo only. |

---
## Validation & Edge Cases

- **IDs required:** Missing `properties.id` (spot) or `checkin_id` (checkin) → error.
- **Coordinates must be geographic:** Values must pass `-90 ≤ lat ≤ 90` and `-180 ≤ lng ≤ 180`.
    - Pixel coords (e.g., from image basemaps) are rejected.
    - Non-Point geometries **without** `properties.lat/lng` are **skipped** (no centroiding).
- **Timestamps:**
    - StraboSpot `modified_timestamp` is **milliseconds since epoch**; converted to UTC.
    - Free-form dates like `"October 19, 2023"` are supported.
- **Photos:** Only the first photo is carried; subsequent photos are ignored in the minimal contract.

---
## CLI test


```bash
cd /interchange-schemas/digitalcrust/interchange_schemas/converter.py
python converter.py checkin2fs /Users/afromandi/Macrostrat/Projects/interchange-schemas/test-data/rockd/checkin-26692.json

python converter.py spot2fs /Users/afromandi/Macrostrat/Projects/interchange-schemas/test-data/strabospot/complete-spot.json
```

### Checkin to FieldSite to Spot
```
afromandi@Amys-MacBook-Air interchange_schemas % python converter.py checkin2fs /interchange-schemas/test-data/rockd/checkin-26692.json

=== FieldSite (from Checkin) ===
{
  "id": 26692,
  "name": null,
  "location": {
    "latitude": 43.6479437702815,
    "longitude": -113.302458592439,
    "elevation": null,
    "radius": null,
    "description": null,
    "closest_place": null,
    "gps_accuracy": null
  },
  "created": "2023-10-19 00:00:00+00:00",
  "updated": "2024-01-13 00:00:00+00:00",
  "observations": [],
  "samples": [],
  "photos": [
    {
      "id": 54284,
      "url": "rockd://photo/54284",
      "width": 0,
      "height": 0,
      "checksum": ""
    }
  ],
  "notes": "Number hill - Mississippian carbonate strata",
  "social": null,
  "children": null,
  "contributors": null
}

=== Spot FeatureCollection (from FieldSite) ===
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -113.302458592439,
          43.6479437702815
        ]
      },
      "properties": {
        "id": 26692,
        "notes": "Number hill - Mississippian carbonate strata",
        "time": "2023-10-19T00:00:00+00:00",
        "lat": 43.6479437702815,
        "lng": -113.302458592439,
        "images": [
          {
            "id": 54284
          }
        ]
      }
    }
  ]
}

```


### Spot to FieldSite to Checkin
```
afromandi@Amys-MacBook-Air interchange_schemas % python converter.py spot2fs /interchange-schemas/test-data/strabospot/complete-spot.json


=== FieldSite (from Spot) ===
{
  "id": 16529992313378,
  "name": null,
  "location": {
    "latitude": 38.576911,
    "longitude": -97.679878,
    "elevation": null,
    "radius": null,
    "description": null,
    "closest_place": null,
    "gps_accuracy": null
  },
  "created": "2022-06-19 22:27:11+00:00",
  "updated": "2022-08-10 16:29:39.966000+00:00",
  "observations": [],
  "samples": [],
  "photos": [
    {
      "id": 16530015128805,
      "url": "rockd://photo/16530015128805",
      "width": 4032,
      "height": 3024,
      "checksum": ""
    }
  ],
  "notes": "Spot notes here",
  "social": null,
  "children": null,
  "contributors": null
}

=== Checkin (from FieldSite) ===
{
  "checkin_id": 16529992313378,
  "notes": "Spot notes here",
  "lat": 38.576911,
  "lng": -97.679878,
  "created": "2022-06-19T22:27:11+00:00",
  "photo": 16530015128805
}

```




---
## Design Notes & Caveats (TBD)

- **Intersection only**: integration stays stable until both sides agree to expand it.
- **First photo only**: keeps interchange small, can change this
- **Non-Point features**: if no lat/lng, skipped (no centroiding).
- **Pixel coordinates**: filtered by geographic validity check.
- **Timestamps**: StraboSpot `modified_timestamp` is ms since epoch → converted to UTC. Free-form date strings like `"October 19, 2023"` supported for Rockd.

---

## Extending Later

When Rockd & StraboSpot agree on more shared semantics (e.g., `name`, multiple photos, `social`, accuracy, altitude, more observation detail):

1. Add fields to `FieldSite` (or un-comment/activate existing optional ones).
    
2. Extend the mapping tables and converter functions accordingly.
    
3. Keep **backwards compatibility** where possible (default values, versioned schemas).
    
4. Update tests and the README tables.
