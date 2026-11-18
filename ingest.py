import duckdb

DB = "fleetsense.duckdb"
MONTHS = [f"2024-{m:02d}" for m in range(1, 13)]
ZONE_URL = "https://d37ci6vzurychx.cloudfront.net/misc/taxi+_zone_lookup.csv"

def get_month_url(month):
    return f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{month}.parquet"

def main():
    con = duckdb.connect(DB)

    # 1. Track what we've already loaded - this makes it idempotent
    con.execute("CREATE TABLE IF NOT EXISTS loaded_months (month VARCHAR PRIMARY KEY)")

    # 2. Load zones - only once
    con.execute("CREATE TABLE IF NOT EXISTS zones AS SELECT * FROM read_csv_auto(?)", [ZONE_URL])
    print(f"Zones: {con.execute('SELECT count(*) FROM zones').fetchone()[0]} rows")

    # 3. Create trips table once
    con.execute("CREATE TABLE IF NOT EXISTS trips AS SELECT * FROM read_parquet(?) LIMIT 0", [get_month_url(MONTHS[0])])

    total_added = 0
    for month in MONTHS:
        already = con.execute("SELECT 1 FROM loaded_months WHERE month = ?", [month]).fetchone()
        if already:
            print(f"{month}: already loaded, skipping - 0 new rows")
            continue

        print(f"{month}: loading...")
        con.execute("INSERT INTO trips SELECT * FROM read_parquet(?)", [get_month_url(month)])
        con.execute("INSERT INTO loaded_months VALUES (?)", [month])
        # Count how many we just added for this month
        added = con.execute("SELECT count(*) FROM trips").fetchone()[0]
        print(f"{month}: done")
        total_added += 1

    final_count = con.execute("SELECT count(*) FROM trips").fetchone()[0]
    print(f"\nDONE. Total trips in DB: {final_count}")
    print(f"Months loaded this run: {total_added} (should be 0 on second run)")
    con.close()

if __name__ == "__main__":
    main()
