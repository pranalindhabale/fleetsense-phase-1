# Release Notes — FleetSense Phase 1 (`v1.0.0`)

**Release Date:** December 2026  
**Project:** FleetSense Phase 1: Data Foundation and Operations Analytics  
**Client:** Ostrander Fieldway Motors  

---

## Overview
Version `v1.0.0` delivers the complete Phase 1 data foundation, business/personal trip segmentation pipeline (CR-1), and interactive operations analytics dashboard built on 12 months of NYC TLC yellow taxi trip records.

---

## What's New

### 1. Data Ingestion & Validation Pipeline
- **12-Month Parquet Ingestion:** Automated ingestion of monthly NYC TLC trip records into DuckDB with SHA-256 file hashing and transaction rollback protection to prevent duplicate or partial loads.
- **Data Cleaning & Quality Rules:** Standardized schema enforcement and automated filtering (`is_analysis_valid`) to remove null timestamps, non-positive fares or trip distances, reversed pickup/dropoff times, and out-of-range taxi zone IDs.

### 2. Core Metrics & CR-1 Trip Segmentation
- **Business vs. Personal Tagging (CR-1):** Implemented client-defined classification rules tagging trips starting on **weekdays (Monday–Friday) between 7:00 AM–10:00 AM and 4:00 PM–7:00 PM** as `business`, and all other trips as `personal`.
- **Demand & Revenue Reporting:** Aggregated trip volume, total revenue, average fare, and hourly/zone-level breakdowns segmented by `business` and `personal` tags.

### 3. Interactive Streamlit Dashboard
- **Filters & Views:** Added interactive date-range and pickup/dropoff zone filters.
- **Operational Analytics:** Built zone-ranked performance tables, hourly demand profiles, and a dedicated **CR-1 Revenue & Demand View** for fleet utilization analysis.

### 4. Documentation & Operational Readiness
- Added `docs/RELEASE_NOTES.md`, `docs/RUNBOOK.md`, and `docs/DATA_QUALITY_REPORT.md` to support reproducible execution and validation.

---

## Known Limitations
- **Historical Proxy Dataset:** Phase 1 uses historical NYC TLC yellow taxi trip records as a proxy dataset prior to connecting live Ostrander Fieldway Motors telematics feeds.
- **Static Business-Hour Window:** CR-1 business hours (`7:00–10:00` and `16:00–19:00` on weekdays) are currently rule-based and do not yet account for public holidays or custom client shift schedules.
- **Local DuckDB Storage:** Designed for single-node local/analytical execution; multi-user concurrent writes are out of scope for Phase 1.
