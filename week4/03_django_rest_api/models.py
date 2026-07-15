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
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="students"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
