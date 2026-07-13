# Write your MySQL query statement below
WITH cte AS (
    SELECT
        user_id,
        prompt,
        tokens,
        AVG(tokens) OVER(PARTITION BY user_id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS avg_tokens
    FROM prompts
)
SELECT
    user_id,
    COUNT(*) AS prompt_count,
    ROUND(avg_tokens, 2) AS avg_tokens
FROM cte
GROUP BY user_id
HAVING prompt_count >= 3 AND COUNT(CASE WHEN tokens > avg_tokens THEN 1 END) >= 1
ORDER BY avg_tokens DESC, user_id
