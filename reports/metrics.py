"""
FleetSense - Metrics Module
Owner: Pranali
Task: Metric definitions for trips, revenue, average fare, duration and utilisation proxy
Client Rule: Business = Weekday + 7-10am OR 4-7pm. Else Personal.
All 5 metrics computed in ONE module, grouped by trip_tag.
"""

import pandas as pd

def load_data(file_path="fleetsense.csv"):
    """Load FleetSense data."""
    df = pd.read_csv(file_path)
    return df

def tag_trip(pickup_weekday, pickup_hour):
    """
    Tag trip as Business or Personal.
    Business = Weekday (Mon-Fri) AND hour 7-10am OR 4-7pm
    Personal = Everything else
    """
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    is_weekday = pickup_weekday in weekdays
    is_business_hour = (7 <= pickup_hour < 10) or (16 <= pickup_hour < 19)

    if is_weekday and is_business_hour:
        return "Business"
    else:
        return "Personal"

def compute_metrics(df):
    """
    Compute 5 metrics grouped by trip_tag.
    1. Trips
    2. Revenue
    3. Average Fare
    4. Duration
    5. Utilisation Proxy
    """
    # 1. Apply tag
    df["trip_tag"] = df.apply(
        lambda row: tag_trip(row["pickup_weekday"], row["pickup_hour"]),
        axis=1
    )

    # 2. Group and compute
    metrics = df.groupby("trip_tag").agg(
        trips=("trip_id", "count"),
        revenue=("fare", "sum"),
        duration=("trip_duration", "mean")
    ).reset_index()

    # 3. Derived metrics
    metrics["average_fare"] = metrics["revenue"] / metrics["trips"]

    # Utilisation Proxy = Trips per hour
    num_hours = df["pickup_hour"].nunique()
    metrics["utilisation_proxy"] = metrics["trips"] / num_hours

    return metrics, df

def main():
    df = load_data("fleetsense.csv")
    metrics, tagged_df = compute_metrics(df)

    print("--- Metrics by Business / Personal ---")
    print(metrics)

    # Save outputs
    metrics.to_csv("metrics_by_tag.csv", index=False)
    tagged_df.to_csv("fleetsense_tagged.csv", index=False)
    print("\nSaved: metrics_by_tag.csv, fleetsense_tagged.csv")

if __name__ == "__main__":
    main()
