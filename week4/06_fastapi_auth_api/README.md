# 06 — FastAPI API with Authentication

**Question this answers:** *How do I protect an endpoint so only logged-in users can use it?*

## File
- `main.py` — register/login endpoints plus a token-protected `/courses` POST route.

## The flow
```
1. POST /register  {email, password}      -> account created
2. POST /login      {email, password}      -> {"access_token": "..."}
3. POST /courses    (Authorization: Bearer <token>)  -> only works with a valid token
   GET  /courses                                      -> open to everyone
```

## Try it
```
pip install fastapi uvicorn
uvicorn main:app --reload
```
Open `http://127.0.0.1:8000/docs` — FastAPI generates an interactive test
page automatically, so you can register, log in, copy the token, and try
the protected endpoint without writing any `curl` commands.

## Why this matters
This mirrors the same register → login → protected-action pattern used in
almost every real API (banking apps, social apps, etc.), just simplified:
instead of industry-standard JWTs, we hand out a random token and keep track
of it in a dictionary. The *concept* — "no token, no access" — is identical.
