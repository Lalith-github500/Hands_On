-- =====================================
-- HANDSON 4 : QUERY OPTIMIZATION
-- =====================================

-- BEFORE INDEX

EXPLAIN
SELECT *
FROM students
WHERE email='rahul@gmail.com';

-- CREATE INDEX

CREATE INDEX idx_email
ON students(email);

-- AFTER INDEX

EXPLAIN
SELECT *
FROM students
WHERE email='rahul@gmail.com';