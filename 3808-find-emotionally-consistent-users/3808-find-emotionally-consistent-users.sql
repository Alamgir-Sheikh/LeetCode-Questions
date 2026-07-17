WITH cte AS (
    SELECT
        user_id,
        reaction,
        COUNT(reaction) AS reaction_count
    FROM reactions
    GROUP BY user_id,reaction
), cte2 AS (
    SELECT
        *,
        SUM(reaction_count) OVER(PARTITION BY user_id)  AS total_reaction,
        ROUND(reaction_count / SUM(reaction_count) OVER(PARTITION BY user_id), 2) AS reaction_ratio
    FROM cte
)
SELECT
    user_id,
    reaction AS dominant_reaction,
    reaction_ratio
FROM cte2
WHERE total_reaction >= 5 AND reaction_ratio >= 0.6
ORDER BY reaction_ratio DESC, user_id