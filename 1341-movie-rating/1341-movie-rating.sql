# Write your MySQL query statement below
SELECT name AS results FROM
(
    SELECT u.name, COUNT(u.user_id) AS rating_count
    FROM Users u
    JOIN MovieRating m
    ON u.user_id = m.user_id
    GROUP BY u.user_id
    ORDER BY rating_count DESC, name ASC
    LIMIT 1
) AS a

UNION ALL
SELECT title AS results FROM (
    SELECT m.title, AVG(mr.rating) AS avg_rate
    FROM Movies m
    JOIN MovieRating mr
    ON m.movie_id = mr.movie_id
    WHERE mr.created_at >= '2020-02-01' AND mr.created_at < '2020-03-01'
    GROUP BY mr.movie_id
    ORDER BY avg_rate DESC, m.title
    LIMIT 1
) AS b
