# Fleetsense - Phase 1

Live NYC Taxi Dashboard built with Streamlit + DuckDB.

**Team:**  Pranali
**Source:** NYC TLC Yellow Taxi Data - Jan 2024 (2.9M rows)

## What it does
- **KPIs:** Total Trips, Total Revenue, Zones
- **Top 10 Pickup Zones:** By trips and revenue
- **Daily Trips Chart:** Daily trend for Jan 2024
- **Filters:** Data Range + Min Trips (Sidebar)

## Tech Stack
- Streamlit
- DuckDB - queries Parquet directly from URL
- Pandas

## How to Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
