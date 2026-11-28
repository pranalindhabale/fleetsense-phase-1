# Data Quality Report — FleetSense Phase 1 (`v1.0.0`)

**Project:** FleetSense Phase 1: Data Foundation and Operations Analytics  
**Client:** Ostrander Fieldway Motors (`Helena Marchetti`)  
**Dataset:** 12-Month NYC TLC Yellow Taxi Trip Records  

---

## 1. Validation Rules & Quality Checks
- **Schema & Timestamp Integrity:** Verified pickup and dropoff timestamps parse cleanly as datetimes and that `dropoff_datetime >= pickup_datetime` (flagging/excluding reversed or zero/negative duration trips).
- **Financial & Distance Sanity:** Checked for `NULL` values, negative or zero fare amounts, negative total amounts, and non-positive or outlier trip distances.
- **Zone & Ingestion Checks:** Validated pickup/dropoff location IDs against valid zone ranges and confirmed monthly ingestion uses file-level hashing and transaction safety to prevent duplicate or partial loads.
- **CR-1 Tagging Verification:** Verified every valid trip receives an explicit `business` or `personal` tag with zero `NULL` or unexpected labels:
  - `business`: Weekday (`Mon`–`Fri`) pickup hour in `07:00–09:59` (`7am–10am`) or `16:00–18:59` (`4pm–7pm`).
  - `personal`: All remaining valid trips (weekends or non-peak weekday hours).

---

## 2. Data Quality Summary (Fill With Your Pipeline Counts)

| Check / Metric | Rule / Criteria | Status | Notes / Row Impact |
|---|---|---|---|
| **Raw Records Ingested** | 12 monthly TLC Parquet files | Verified | Replace with total raw row count |
| **Invalid / Outlier Trips Excluded** | Nulls, bad timestamps, invalid fare/distance/zone | Filtered | Replace with excluded count & % |
| **Analysis-Ready Trips (`is_analysis_valid`)** | Clean trips used for demand & revenue metrics | Verified | Replace with valid row count & % |
| **CR-1 Tag Completeness** | `business` vs. `personal` assigned to all valid trips | 100% Tagged | Confirm 0 nulls in CR-1 column |

---

## 3. Risks & Recommendations for Operations
- **Upstream Flag Trust:** Re-validate core fields (`pickup_datetime`, `dropoff_datetime`, fare, distance, zone IDs) rather than relying solely on pre-computed flags.
- **Holiday & Shift Rules:** Confirm with Ostrander Fieldway Motors whether holidays or shift exceptions should modify the weekday `7am–10am` and `4pm–7pm` business rule in future releases.
