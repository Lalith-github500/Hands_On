# 01 — Django Basic Endpoint

**Question this answers:** *How do I create a working web endpoint in Django?*

## Files
- `views.py` — one function that returns a JSON response.
- `urls.py` — routes the URL `/status/` to that function.

## How it fits together
```
Browser/Client  --GET /status/-->  urls.py  -->  views.py  --> JSON response
```

## To actually run this
These two files plug into a normal Django project (`django-admin startproject`).
Drop them into an app, add the app's `urls.py` to your project's root
`urls.py` with `path("", include("courses.urls"))`, then run:
```
python manage.py runserver
```
and visit `http://127.0.0.1:8000/status/`.
