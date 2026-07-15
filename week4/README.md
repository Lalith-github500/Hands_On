# Week 4 — Building the Same "Course Management API" Three Ways

This folder walks through building a small **Course Management API** using three
popular Python web frameworks, in increasing order of complexity. Each subfolder
is self-contained and has its own README explaining what it does and how to run it.

| Folder | Framework | What it teaches |
|---|---|---|
| `01_django_basic_endpoint` | Django | Your first view + URL route |
| `02_django_course_models` | Django | Defining database models & relationships |
| `03_django_rest_api` | Django REST Framework | Turning models into a full CRUD API |
| `04_flask_inmemory_api` | Flask | A minimal API with no database (data lives in a list) |
| `05_flask_sqlalchemy_api` | Flask + SQLAlchemy | Same API, now backed by a real database |
| `06_fastapi_auth_api` | FastAPI | A modern async API with signup/login + protected routes |

**Suggested order:** read them 01 → 06. Each step only adds *one* new idea on top
of the last one, so by the end you'll understand routing, models, serialization,
databases, and authentication — without ever facing more than one new concept
at a time.
