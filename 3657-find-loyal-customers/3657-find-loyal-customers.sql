# Write your MySQL query statement below
WITH filtered_data AS (
    SELECT 
        customer_id,
        COUNT(CASE WHEN transaction_type = 'purchase' THEN 1 END) AS total_purchase_transaction,
        DATEDIFF(MAX(transaction_date), MIN(transaction_date)) AS active_days,
        COUNT(CASE WHEN transaction_type = 'refund' THEN 1 END) / COUNT(*) AS refund_rate
    FROM customer_transactions
    GROUP BY customer_id
)
SELECT 
    customer_id
FROM filtered_data
WHERE total_purchase_transaction >= 3 AND active_days >= 30 AND refund_rate < 0.2
ORDER BY customer_id