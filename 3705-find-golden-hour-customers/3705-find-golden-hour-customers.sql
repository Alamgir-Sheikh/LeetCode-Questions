# Write your MySQL query statement below
WITH new_data AS (
    SELECT
        customer_id,
        COUNT(*) AS total_orders,
        COUNT(CASE WHEN DATE_FORMAT(order_timestamp, "%H:%i") BETWEEN "11:00" AND "14:00" 
            OR DATE_FORMAT(order_timestamp, "%H:%i") BETWEEN "18:00" AND "21:00" THEN 1 END) AS peak_order_count,
        ROUND(AVG(order_rating), 2) AS average_rating,
        COUNT(CASE WHEN order_rating IS NOT NULL THEN 1 END) / COUNT(*) AS rating_percentage
    FROM restaurant_orders
    GROUP BY customer_id
    HAVING peak_order_count / total_orders >= 0.6
)

-- SELECT customer_id,
--     total_orders,
--     peak_order_count,
--     (peak_order_count / total_orders) * 100 AS peak_hour_percentage,
--     (peak_order_count / total_orders) AS peak_percentage,
--     average_rating,
--     rating_percentage
-- FROM new_data


SELECT customer_id,
    total_orders,
    ROUND((peak_order_count / total_orders) * 100) AS peak_hour_percentage,
    average_rating
FROM new_data
WHERE total_orders >= 3 AND average_rating >= 4 AND rating_percentage >= 0.5
ORDER BY average_rating DESC, customer_id DESC