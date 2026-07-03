-- -- # Write your MySQL query statement below

-- WITH store_data AS (
--     SELECT product_id , CASE WHEN store1 IS NOT NULL THEN 'store1' END AS store FROM Products
--     UNION ALL
--     SELECT product_id , CASE WHEN store2 IS NOT NULL THEN 'store2' END AS store FROM Products
--     UNION ALL
--     SELECT product_id , CASE WHEN store3 IS NOT NULL THEN 'store3' END AS store FROM Products
-- ), price_data AS (
--     SELECT product_id , CASE WHEN store1 IS NOT NULL THEN store1 END AS price FROM Products
--     UNION ALL
--     SELECT product_id , CASE WHEN store2 IS NOT NULL THEN store2 END AS price FROM Products
--     UNION ALL
--     SELECT product_id , CASE WHEN store3 IS NOT NULL THEN store3 END AS price FROM Products
-- )
-- -- SELECT * FROM price_data WHERE price IS NOT NULL;

-- SELECT * FROM store_data WHERE store IS NOT NULL



WITH store_data AS (
    SELECT product_id , CASE WHEN store1 IS NOT NULL THEN 'store1' END AS store, CASE WHEN store1 IS NOT NULL THEN store1 END AS price FROM Products
    UNION ALL
    SELECT product_id , CASE WHEN store2 IS NOT NULL THEN 'store2' END AS store, CASE WHEN store2 IS NOT NULL THEN store2 END AS price FROM Products
    UNION ALL
    SELECT product_id , CASE WHEN store3 IS NOT NULL THEN 'store3' END AS store, CASE WHEN store3 IS NOT NULL THEN store3 END AS price FROM Products
)
SELECT * FROM store_data
WHERE price IS NOT NULL OR store IS NOT NULL