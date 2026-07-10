# Write your MySQL query statement below

WITH ranked_ratings AS (
    SELECT *,
        LEAD(rating) OVER(PARTITION BY employee_id ORDER BY review_date DESC) AS l1,
        LEAD(rating, 2) OVER(PARTITION BY employee_id ORDER BY review_date DESC) AS l2,
        ROW_NUMBER() OVER(PARTITION BY employee_id ORDER BY review_date DESC) AS rn
    FROM performance_reviews
)

-- SELECT * FROM ranked_ratings

SELECT DISTINCT r.employee_id, e.name, (r.rating - r.l2) AS improvement_score
FROM ranked_ratings r
JOIN employees e
ON r.employee_id = e.employee_id
WHERE rn = 1 AND (rating > l1 AND l1 > l2)
ORDER BY improvement_score DESC, name




