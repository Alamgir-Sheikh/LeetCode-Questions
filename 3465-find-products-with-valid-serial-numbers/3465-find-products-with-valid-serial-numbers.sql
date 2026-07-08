# Write your MySQL query statement below
SELECT *
FROM Products
WHERE REGEXP_LIKE(description, '(^|[:space:]|[^[:alnum:]])SN[0-9]{4}-[0-9]{4}($|[:space:]|[^[:alnum:]])', 'c')
ORDER BY product_id