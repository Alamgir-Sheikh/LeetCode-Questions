# Write your MySQL query statement below
WITH polarized_data AS (
    SELECT 
        book_id,
        COUNT(CASE WHEN session_rating <= 2 THEN 1 END) AS low_polarized,
        COUNT(CASE WHEN session_rating >= 4 THEN 1 END) AS high_polarized, 
        MAX(session_rating) - MIN(session_rating) AS rating_spread,
        ROUND(SUM(CASE WHEN session_rating <= 2 OR session_rating >= 4 THEN 1 ELSE 0 END) / COUNT(*), 2) AS polarization_score
    FROM reading_sessions
    GROUP BY book_id
    HAVING COUNT(*) >= 5 AND (low_polarized >= 1 AND high_polarized >= 1)
)
SELECT 
    p.book_id,
    b.title,
    b.author,
    b.genre,
    b.pages,
    p.rating_spread,
    p.polarization_score
FROM polarized_data p
JOIN Books b
ON p.book_id = b.book_id
WHERE polarization_score >= 0.6
ORDER BY polarization_score DESC, title DESC