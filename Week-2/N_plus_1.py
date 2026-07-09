# N+1 QUERY PROBLEM

students = session.query(Student).all()

for student in students:
    print(student.department.dept_name)

#Solution
from sqlalchemy.orm import joinedload

students = (
    session.query(Student)
    .options(joinedload(Student.department))
    .all()
)
