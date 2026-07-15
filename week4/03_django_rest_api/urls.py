"""
Goal: register our ViewSets with a DRF router, which auto-generates
all the URL patterns (list, create, retrieve, update, delete) for us.
"""
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CourseViewSet, StudentViewSet

router = DefaultRouter()
router.register("courses", CourseViewSet)
router.register("students", StudentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
