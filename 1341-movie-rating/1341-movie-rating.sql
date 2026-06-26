# Write your MySQL query statement below
WITH names AS (
    SELECT u.name, COUNT(mr.user_id) AS rating_count
    FROM MovieRating mr
    INNER JOIN Users u
    ON mr.user_id = u.user_id
    GROUP BY mr.user_id
    ORDER BY rating_count DESC, name
    LIMIT 1
), avg_rating AS (
    SELECT m.title, AVG(rating) AS avg_rate
    FROM MovieRating mr
    JOIN Movies m
    ON m.movie_id = mr.movie_id
    WHERE MONTH(created_at) = 2 AND YEAR(created_at) = 2020
    GROUP BY mr.movie_id
    ORDER BY avg_rate DESC, m.title
    LIMIT 1
)

-- SELECT * FROM avg_rating

SELECT name AS results FROM names
UNION ALL
SELECT title AS rsults FROM avg_rating;