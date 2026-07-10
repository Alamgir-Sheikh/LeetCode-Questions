WITH borrowed_books AS (
    SELECT book_id, COUNT(book_id) AS current_borrowers
    FROM Borrowing_Records
    WHERE return_date IS NULL
    GROUP BY book_id
)
SELECT br.book_id, lb.title, lb.author, lb.genre, lb.publication_year, br.current_borrowers
FROM borrowed_books br
INNER JOIN library_books lb
ON br.book_id = lb.book_id
WHERE lb.total_copies - br.current_borrowers = 0
ORDER BY current_borrowers DESC, title