# Write your MySQL query statement below
WITH efficiency_data AS (
    SELECT 
        driver_id,
        trip_date,
        AVG(CASE WHEN trip_date >= '2023-01-01' AND trip_date < '2023-07-01' THEN (distance_km / fuel_consumed) END) AS first_half_avg,
        AVG(CASE WHEN trip_date >= '2023-07-01' AND trip_date <= '2023-12-31' THEN (distance_km / fuel_consumed) END) AS second_half_avg
    FROM trips
    GROUP BY driver_id
)
SELECT 
    e.driver_id, d.driver_name, 
    ROUND(e.first_half_avg, 2) AS first_half_avg, 
    ROUND(e.second_half_avg, 2) AS  second_half_avg, 
    ROUND((e.second_half_avg - e.first_half_avg), 2) AS efficiency_improvement
FROM efficiency_data e
JOIN drivers d
ON e.driver_id = d.driver_id
WHERE first_half_avg < second_half_avg
ORDER BY efficiency_improvement DESC, driver_name 