-- =====================================
-- HANDSON 2 : DML, JOINS, AGGREGATION
-- =====================================

-- INSERT

INSERT INTO departments VALUES
(1,'Computer Science'),
(2,'Electronics');

INSERT INTO students VALUES
(101,'Rahul','rahul@gmail.com',1),
(102,'Priya','priya@gmail.com',2);

INSERT INTO professors VALUES
(1,'Dr Kumar',1),
(2,'Dr Ravi',2);

INSERT INTO courses VALUES
(201,'Database Systems',4,1),
(202,'Digital Electronics',3,2);

INSERT INTO enrollments VALUES
(1,101,201,'2025-07-01'),
(2,102,202,'2025-07-01');

-- UPDATE

UPDATE students
SET email='rahul123@gmail.com'
WHERE student_id=101;

-- DELETE

DELETE FROM enrollments
WHERE enrollment_id=2;

-- FILTER

SELECT *
FROM students
WHERE dept_id=1;

-- SORT

SELECT *
FROM students
ORDER BY student_name;

-- INNER JOIN

SELECT s.student_name,c.course_name
FROM students s
JOIN enrollments e
ON s.student_id=e.student_id
JOIN courses c
ON e.course_id=c.course_id;

-- LEFT JOIN

SELECT s.student_name,e.course_id
FROM students s
LEFT JOIN enrollments e
ON s.student_id=e.student_id;

-- GROUP BY

SELECT dept_id,COUNT(*) AS total_students
FROM students
GROUP BY dept_id;

-- HAVING

SELECT dept_id,COUNT(*) AS total_students
FROM students
GROUP BY dept_id
HAVING COUNT(*) > 0;