"""
Goal: create the smallest possible Django "view" — a Python function that
takes a web request and returns a web response.

Nothing about databases yet. Just: request comes in -> response goes out.
"""
from django.http import JsonResponse


def status_check(request):
    """
    Visiting /status/ in the browser will run this function.
    We return JSON (instead of plain text) because almost every real API
    returns JSON, so it's good to get used to it from the start.
    """
    return JsonResponse({
        "status": "ok",
        "message": "Course Management API is running",
    })
