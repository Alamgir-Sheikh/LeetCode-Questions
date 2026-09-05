# Write your MySQL query statement below
WITH OrdersCount As (
    SELECT customer_number, COUNT(customer_number) AS order_count
    FROM Orders
    GROUP BY customer_number
)
SELECT customer_number 
FROM OrdersCount
WHERE order_count = (SELECT MAX(order_count) FROM OrdersCount);