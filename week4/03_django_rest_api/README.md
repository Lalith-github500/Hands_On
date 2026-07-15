# 03 — Django REST API

**Question this answers:** *How do I expose my models as a full JSON CRUD API without writing repetitive code?*

## Files
- `models.py` — same `Course`/`Student` models as step 02.
- `serializers.py` — turns model instances into JSON and back.
- `views.py` — `ModelViewSet`s that give you Create/Read/Update/Delete for free,
  plus one custom endpoint: `GET /courses/{id}/students/`.
- `urls.py` — a `DefaultRouter` that wires up all the URLs automatically.

## Endpoints you get automatically
| Method | URL | Action |
|---|---|---|
| GET | `/courses/` | list all courses |
| POST | `/courses/` | create a course |
| GET | `/courses/{id}/` | get one course |
| PUT | `/courses/{id}/` | update a course |
| DELETE | `/courses/{id}/` | delete a course |
| GET | `/courses/{id}/students/` | list students in that course |
| GET/POST/PUT/DELETE | `/students/...` | same pattern for students |

## Why this matters
Compare this to step 01: back then, *we* wrote the route and the function
by hand. Here, one `router.register(...)` line generates 5+ routes. This is
the payoff of using a framework's built-in tools instead of doing everything
manually.
