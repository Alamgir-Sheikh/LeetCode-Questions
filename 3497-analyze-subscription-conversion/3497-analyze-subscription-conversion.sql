# Write your MySQL query statement below
WITH activity_data AS (
    SELECT user_id,
        ROUND(AVG(CASE WHEN activity_type = 'free_trial' THEN activity_duration END), 2) AS trial_avg_duration,
        ROUND(AVG(CASE WHEN activity_type = 'paid' THEN activity_duration END), 2) AS paid_avg_duration
    FROM UserActivity
    GROUP BY user_id
)
SELECT *
FROM activity_data
WHERE paid_avg_duration IS NOT NULL