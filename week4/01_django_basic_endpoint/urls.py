"""
Goal: connect a URL (web address) to the view function we just wrote.

Django keeps "what URL" and "what code runs" in separate files on purpose —
it makes it easy to see every route your app supports in one place.
"""
from django.urls import path

from .views import status_check

urlpatterns = [
    # Visiting /status/ will call status_check() from views.py
    path("status/", status_check, name="status-check"),
]
