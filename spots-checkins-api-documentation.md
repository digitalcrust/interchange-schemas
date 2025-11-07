# Spots ↔ FieldSites ↔ Checkins API

**Base URL:** `http://dev.macrostrat.org/api/v3/dev/convert/`

**Endpoint:** `POST field-site?in=<spot|fieldsite>&out=<fieldsite|checkin>`

- **Content-Type:** `application/json`
- **Accept:** `application/json`

---

## Supported Conversions

- `in=spot&out=fieldsite` — Convert StraboSpot **FeatureCollection(s)** → array of **FieldSite** objects
- `in=fieldsite&out=checkin` — Convert **FieldSite** array → array of **Rockd checkin** objects
- `in=spot&out=checkin` — Direct pipeline: **FeatureCollection(s)** → FieldSite(s) → Checkin(s)

> Non-Point features (e.g., LineString/Polygon) are ignored during `spot → fieldsite` extraction.  
> Spots with `image_basemap` are also ignored.  
> Point coordinates must be valid lon/lat pairs (−180..180, −90..90).

---

## Request & Response Examples

### 1) `in=spot&out=fieldsite`

**Request Body:** *FeatureCollection* (or array of FeatureCollections)

<details><summary><strong>Minimal FeatureCollection</strong></summary>

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": { "type": "Point", "coordinates": [-97.679878, 38.576911] },
      "properties": {
        "id": 16529992313378,
        "time": "2022-06-19T22:27:11.000Z",
        "modified_timestamp": 1660148995221,
        "notes": "Optional notes",
        "images": [{ "id": 16530015128805, "width": 4032, "height": 3024 }]
      }
    }
  ]
}
```
</details>


**Success Response:** `200 OK` — array of **FieldSite**

```json
[
  {
    "id": 16529992313378,
    "name": null,
    "location": { "latitude": 38.576911, "longitude": -97.679878, "elevation": null, "radius": null, "description": null, "closest_place": null, "gps_accuracy": null },
    "created": "2022-06-19T22:27:11+00:00",
    "updated": "2022-08-10T16:29:55+00:00",
    "observations": [
      { "notes": null, "data": { "strike": 123.0, "dip": 45.0, "facing": "upright", "notes": null, "associated": [] } }
    ],
    "samples": [],
    "photos": [
      { "id": 16530015128805, "url": "rockd://photo/16530015128805", "width": 4032, "height": 3024, "checksum": "" }
    ],
    "notes": "Optional notes",
    "social": null,
    "children": null,
    "contributors": null
  }
]
```

---

### 2) `in=fieldsite&out=checkin`

**Request Body:** array of **FieldSite**

<details><summary><strong>Minimal FieldSite array</strong></summary>

```json
[
  {
    "id": 16529992313378,
    "name": null,
    "location": { "latitude": 38.576911, "longitude": -97.679878 },
    "created": "2022-06-19T22:27:11Z",
    "updated": "2022-08-10T16:29:39.966000Z",
    "observations": [
      { "data": { "strike": 123.0, "dip": 45.0, "facing": "upright" } }
    ],
    "photos": [{ "id": 16530015128805, "url": "rockd://photo/16530015128805", "width": 4032, "height": 3024, "checksum": "" }],
    "notes": "Spot notes here"
  }
]
```
</details>

**Success Response:** `200 OK` — array of **Checkin**

```json
[
  {
    "checkin_id": 16529992313378,
    "notes": "Spot notes here",
    "lat": 38.576911,
    "lng": -97.679878,
    "created": "2022-06-19T22:27:11+00:00",
    "photo": 16530015128805,
    "observations": [ { "orientation": { "strike": 123.0, "dip": 45.0 } } ]
  }
]
```

**Notes**
- If `observations[].data` contains a planar orientation (numeric `strike` and `dip`), it is mapped into `observations[].orientation` in the output.
- If a `photos` array exists, the first photo’s `id` is mapped to `photo`.
- `created` and `updated` accept ISO strings or common date strings (best-effort parse).

---

### 3) `in=spot&out=checkin`

Pipeline: `FeatureCollection(s) → FieldSite(s) → Checkin(s)`

**Request Body:** *FeatureCollection* (same as #1)

**Success Response:** `200 OK` — array of **Checkin** (same shape as #2)

---

## Field Mapping Summary

- **Spot → FieldSite**
  - `properties.id` → `FieldSite.id` *(required)*
  - `geometry.coordinates` (Point) → `FieldSite.location.longitude/latitude`  
    - If `properties.lng/lat` exist, those are used; otherwise pulled from geometry.
  - `properties.time | properties.date` → `FieldSite.created` (parsed)
  - `properties.modified_timestamp` (ms) → `FieldSite.updated` (parsed); fallback `created`
  - First `properties.images[0]` → `FieldSite.photos[0]` (id/width/height)
  - First planar in `properties.orientation_data[]` → `FieldSite.observations[0].data` as `{ strike, dip, facing: "upright" }`
  - Ignored: non-Point features; features with `image_basemap`

- **FieldSite → Checkin**
  - `id` → `checkin_id`
  - `location.latitude/longitude` → `lat`/`lng`
  - `created` → `created` (ISO)
  - `photos[0].id` → `photo` (optional)
  - First `observations[].data` that is planar → `observations[0].orientation.{strike,dip}`

---

## Error Responses

- `400 Bad Request` — missing/invalid `in`/`out`, invalid geometry/coords
- `200 OK` with empty array — when no qualifying Point features are found
- `500 Internal Server Error` — unexpected serialization or schema issues
