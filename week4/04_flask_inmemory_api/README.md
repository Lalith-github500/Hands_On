# 04 — Flask In-Memory API

**Question this answers:** *How do I build a simple JSON API without any database, and validate input from the client?*

## File
- `app.py` — everything in one file: routes, storage, and validation.

## Endpoints
| Method | URL | Action |
|---|---|---|
| GET | `/courses` | list all courses (empty at first) |
| POST | `/courses` | add a course (requires `name`, `code`, `credits` in the JSON body) |

## Try it
```
python app.py
```
Then, in another terminal:
```
curl http://127.0.0.1:5000/courses

curl -X POST http://127.0.0.1:5000/courses \
     -H "Content-Type: application/json" \
     -d '{"name": "Python Basics", "code": "PY101", "credits": 3}'
```
## Why this matters
Flask doesn't force any project structure on you — one file is a complete,
working app. That's the tradeoff versus Django: less setup, but you write
more of the plumbing yourself (like the validation check above).
