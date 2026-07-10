WITH first_positive_records AS (
    SELECT
        patient_id,
        MIN(CASE WHEN result = 'Positive' THEN test_date END) AS first_positive
    FROM covid_tests
    GROUP BY patient_id
), first_negative_records AS (
    SELECT
        c.patient_id,
        DATEDIFF(MIN(CASE WHEN c.result = 'Negative' AND c.test_date > f.first_positive THEN test_date END), f.first_positive) AS recovery_time
    FROM covid_tests c
    JOIN first_positive_records f
    ON c.patient_id = f.patient_id
    GROUP BY c.patient_id
)
SELECT f.patient_id, p.patient_name, p.age, f.recovery_time 
FROM first_negative_records f
INNER JOIN  patients p
ON f.patient_id = p.patient_id AND f.recovery_time IS NOT NULL
ORDER BY recovery_time, patient_name
