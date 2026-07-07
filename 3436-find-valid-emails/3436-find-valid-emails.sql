# Write your MySQL query statement below
SELECT
    user_id,
    email
FROM Users
WHERE REGEXP_LIKE(email, "^[A-Za-z0-9]+[A-Za-z0-9_]*@[a-z]+\\.com$")
ORDER BY user_id