WITH expensive_product AS (
    SELECT store_id,
        quantity,
        product_name,
        price,
        ROW_NUMBER() OVER(PARTITION BY store_id ORDER BY price DESC) AS exp_rn,
        COUNT(product_name) OVER(PARTITION BY store_id) AS product_count
    FROM Inventory
), cheap_product AS (
    SELECT store_id,
        quantity,
        product_name,
        price,
        ROW_NUMBER() OVER(PARTITION BY store_id ORDER BY price) AS cheap_rn
    FROM Inventory
), exp_cheap_product AS (
    SELECT 
        e.store_id,
        e.product_name AS most_exp_product,
        c.product_name AS cheapest_product,
        ROUND(c.quantity / e.quantity , 2) AS imbalance_ratio
    FROM expensive_product e
    INNER JOIN cheap_product c
    ON e.store_id = c.store_id
    WHERE c.quantity > e.quantity AND e.product_count > 2 AND (exp_rn = 1 AND cheap_rn = 1)
)
-- SELECT * FROM expensive_product
-- SELECT * FROM cheap_product
SELECT 
    s.store_id,
    s.store_name,
    s.location,
    e.most_exp_product,
    e.cheapest_product,
    e.imbalance_ratio
FROM exp_cheap_product e
JOIN Stores s
ON e.store_id = s.store_id
ORDER BY imbalance_ratio DESC, store_name