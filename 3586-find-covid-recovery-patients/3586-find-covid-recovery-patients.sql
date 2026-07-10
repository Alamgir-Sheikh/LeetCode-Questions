with positive AS(
    SELECT patient_id, MIN(test_date) AS first_positive_date
    FROM covid_tests
    WHERE result = 'Positive'
    GROUP BY patient_id
), negative AS (
    SELECT c.patient_id, MIN(c.test_date) AS first_negative_date
    FROM covid_tests c
    INNER JOIN positive tp
    ON c.patient_id = tp.patient_id
    WHERE result = 'Negative' AND c.test_date > tp.first_positive_date
    GROUP BY patient_id
)
SELECT p.patient_id, pa.patient_name, pa.age, DATEDIFF(n.first_negative_date, p.first_positive_date) AS recovery_time
FROM positive p
INNER JOIN negative n
ON p.patient_id = n.patient_id
INNER JOIN
patients pa
ON pa.patient_id = p.patient_id
ORDER BY recovery_time, patient_name