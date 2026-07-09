# Write your MySQL query statement below
WITH season_data AS (
    SELECT
        s.quantity,s.price,p.category, (s.quantity * s.price) AS revenue,
        CASE
            WHEN MONTH(s.sale_date) >= '3' AND MONTH(s.sale_date) < '06' THEN 'Spring'
            WHEN MONTH(s.sale_date) >= '06' AND MONTH(s.sale_date) < '09' THEN 'Summer'
            WHEN MONTH(s.sale_date) >= '09' AND MONTH(s.sale_date) < '12' THEN 'Fall'
            ELSE 'Winter' END AS season
        FROM Sales s
        JOIN Products p
        ON s.product_id = p.product_id
        ORDER BY season
), revenue_data AS (
    SELECT season,category,SUM(quantity) AS total_quantity, ROUND(SUM(revenue),2) AS total_revenue 
    FROM season_data
    GROUP BY season,category
    ORDER BY season
)



SELECT season, category, total_quantity, total_revenue 
FROM (
    SELECT *,
        DENSE_RANK() OVER(PARTITION BY season ORDER BY total_quantity DESC, total_revenue DESC) AS dnk
    FROM revenue_data
) a
WHERE a.dnk = 1
ORDER BY season