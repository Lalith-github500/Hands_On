# 05 — Flask + SQLAlchemy API

**Question this answers:** *How do I persist data to a real database instead of losing it on restart?*

## Files
- `models.py` — the `Course` table, defined with Flask-SQLAlchemy, plus a
  `to_dict()` helper for turning a row into JSON.
- `app.py` — the same two routes as step 04, but now reading from and
  writing to an actual SQLite file (`courses.db`).

## What changed from step 04
| Step 04 | Step 05 |
|---|---|
| `courses = []` (Python list) | `courses.db` (SQLite file) |
| Data lost on restart | Data survives restart |
| Manual dict building | `Course.to_dict()` |

## Try it
```
pip install flask flask_sqlalchemy
python app.py
```
Then repeat the same `curl` commands from step 04 — but this time, stop and
restart `app.py` and your courses will still be there.
