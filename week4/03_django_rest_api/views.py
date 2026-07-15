"""
Goal: get a full CRUD API (Create, Read, Update, Delete) for Course and
Student almost for free, using DRF's ModelViewSet.

A ModelViewSet automatically wires up:
    GET    /courses/        -> list all courses
    POST   /courses/        -> create a course
    GET    /courses/{id}/   -> retrieve one course
    PUT    /courses/{id}/   -> update one course
    DELETE /courses/{id}/   -> delete one course
...and the same for /students/.
"""
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Course, Student
from .serializers import CourseSerializer, StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=["get"])
    def students(self, request, pk=None):
        """
        Custom extra endpoint: GET /courses/{id}/students/
        Returns every student enrolled in this one course.
        """
        course = self.get_object()
        serializer = StudentSerializer(course.students.all(), many=True)
        return Response(serializer.data)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
