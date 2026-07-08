# Write your MySQL query statement below
WITH details AS (
    SELECT p.user_id, p.product_id, i.category
    FROM ProductPurchases p
    JOIN ProductInfo i
    ON p.product_id = i.product_id
),paired_product AS (
    SELECT
        p1.product_id AS product1_id, 
        p2.product_id AS product2_id,
        p1.category AS product1_category,
        p2.category AS product2_category
    FROM details p1
    LEFT JOIN details p2
    ON p1.user_id = p2.user_id AND p1.product_id < p2.product_id
)
SELECT product1_id, product2_id, product1_category, product2_category, COUNT(*) AS customer_count
FROM paired_product
WHERE product2_id IS NOT NULL
GROUP BY product1_id, product2_id, product1_category, product2_category
HAVING customer_count >= 3
ORDER BY customer_count DESC, product1_id, product2_id

