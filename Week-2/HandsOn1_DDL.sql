-- =====================================
-- HANDSON 1 : SCHEMA DESIGN (DDL)
-- =====================================

-- CREATE TABLES

CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL
);

CREATE TABLE professors (
    professor_id INT PRIMARY KEY,
    professor_name VARCHAR(100),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    email VARCHAR(100),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    credits INT,
    professor_id INT,
    FOREIGN KEY (professor_id)
    REFERENCES professors(professor_id)
);

CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    FOREIGN KEY (student_id)
    REFERENCES students(student_id),
    FOREIGN KEY (course_id)
    REFERENCES courses(course_id)
);

-- ALTER TABLE : ADD COLUMN

ALTER TABLE students
ADD phone VARCHAR(15);

-- ALTER TABLE : RENAME COLUMN

ALTER TABLE students
RENAME COLUMN phone TO mobile_no;

-- ALTER TABLE : DROP COLUMN

ALTER TABLE students
DROP COLUMN mobile_no;

-- ADD CHECK CONSTRAINT

ALTER TABLE courses
ADD CONSTRAINT chk_credits
CHECK (credits > 0);