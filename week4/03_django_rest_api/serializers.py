"""
Goal: convert model instances <-> JSON automatically.

Without DRF, you'd have to manually write code like:
    {"id": course.id, "name": course.name, "code": course.code, ...}
for every model, every time. A Serializer does that for you.
"""
from rest_framework import serializers

from .models import Course, Student


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"  # turn every model field into a JSON field


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
