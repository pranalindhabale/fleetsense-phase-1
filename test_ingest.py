import duckdb
con = duckdb.connect("fleetsense.duckdb", read_only=True)
before = con.execute("SELECT count(*) FROM trips").fetchone()[0]
print(f"Row count before: {before}")
print(f"Loaded months: {con.execute('SELECT count(*) FROM loaded_months').fetchone()[0]} / 12")
print("If you run ingest.py again, this number must NOT change.")
