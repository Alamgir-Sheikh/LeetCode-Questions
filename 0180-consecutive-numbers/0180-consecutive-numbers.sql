# Write your MySQL query statement below
WITH nums AS (
    SELECT num,
    LEAD(num) OVER(ORDER BY id) AS l1,
    LEAD(num, 2) OVER(ORDER BY id) AS l2
    FROM Logs
)
SELECT DISTINCT num AS ConsecutiveNums
FROM nums
WHERE num = l1 AND l1 = l2