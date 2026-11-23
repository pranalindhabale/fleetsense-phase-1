# Metric Definitions - FleetSense

## 1. Trip Tag Rule (Client Rule - Helena)

Every trip is tagged as **Business** or **Personal**.

- **Business** = Pickup on Weekday (Monday to Friday) AND Pickup Hour is 7-10am OR 4-7pm
- **Personal** = All other trips

Demand and Revenue are reported separately for Business and Personal.

## 2. Metric Definitions

### 1. Trips
**Definition:** Total number of trips in the period.
**Formula:** `Count(trip_id)`

### 2. Revenue
**Definition:** Total money earned from fares.
**Formula:** `Sum(fare)`

### 3. Average Fare
**Definition:** Average money earned per trip.
**Formula:** `Revenue / Trips`

### 4. Duration
**Definition:** Average time of a trip in minutes.
**Formula:** `Average(trip_duration)`

### 5. Utilisation Proxy
**Definition:** How busy the fleet is. Trips per hour.
**Formula:** `Trips / Number of Hours in Period`

## 3. Where is it computed?
All 5 metrics are computed in ONE module: `src/metrics.py`
Grouped by `trip_tag` (Business / Personal).

## 4. Owner
BA: Pranali
Due: Fri 27 Nov
