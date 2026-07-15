"""
Goal: describe the shape of our data using Django models.

Each class below becomes a database table. Each attribute becomes a column.
We keep it to 3 models (instead of 4+) so the relationships stay easy to follow:

    Course  <---- (many)  Student  (each student belongs to one course)

That's it — one relationship, one direction. Once this makes sense, adding
more tables (like Department or Enrollment) is just repeating the same pattern.
"""
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=20, unique=True)
    credits = models.IntegerField()

    def __str__(self):
        return f"{self.code} - {self.name}"


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    # This is the important line: it links a Student to one Course.
    # related_name="students" lets us write `some_course.students.all()`
    # to get every student enrolled in that course.
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="students"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
