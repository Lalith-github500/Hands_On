# 02 — Django Course Models

**Question this answers:** *How do I represent related data (courses and their students) as database tables?*

## Files
- `models.py` — defines `Course` and `Student`, linked by a `ForeignKey`.

## Key idea
A `ForeignKey` on `Student` pointing at `Course` means: *"each student
belongs to exactly one course, but a course can have many students."*
This is the most common relationship in web apps, so it's worth understanding
well before moving on to more complex ones.

## To actually run this
```
python manage.py makemigrations
python manage.py migrate
```
Then, in the Django shell (`python manage.py shell`):
```python
from courses.models import Course, Student

c = Course.objects.create(name="Python Basics", code="PY101", credits=3)
Student.objects.create(first_name="Ana", last_name="Rao", email="ana@example.com", course=c)

c.students.all()  # -> shows every student enrolled in this course
```
