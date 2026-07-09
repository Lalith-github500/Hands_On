-- =====================================
-- HANDSON 3 : ADVANCED SQL
-- =====================================

-- SUBQUERY

SELECT student_name
FROM students
WHERE dept_id =
(
    SELECT dept_id
    FROM departments
    WHERE dept_name='Computer Science'
);

-- VIEW

CREATE VIEW student_courses AS
SELECT s.student_name,
       c.course_name
FROM students s
JOIN enrollments e
ON s.student_id=e.student_id
JOIN courses c
ON e.course_id=c.course_id;

SELECT * FROM student_courses;

-- USER DEFINED FUNCTION

CREATE FUNCTION get_course_count()
RETURNS INTEGER
AS $$
BEGIN
    RETURN (SELECT COUNT(*) FROM courses);
END;
$$ LANGUAGE plpgsql;

SELECT get_course_count();

-- TRANSACTION + COMMIT

BEGIN;

INSERT INTO students
VALUES (103,'Anu','anu@gmail.com',1);

COMMIT;

-- TRANSACTION + ROLLBACK

BEGIN;

INSERT INTO students
VALUES (104,'Test','test@gmail.com',1);

ROLLBACK;

-- SAVEPOINT

BEGIN;

INSERT INTO students
VALUES (105,'Arun','arun@gmail.com',1);

SAVEPOINT sp1;

INSERT INTO students
VALUES (106,'Kiran','kiran@gmail.com',1);

ROLLBACK TO sp1;

COMMIT;