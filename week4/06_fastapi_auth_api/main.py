"""
Goal: build a modern async API with FastAPI, and protect one route so only
"logged in" users can use it.

To keep the *auth* idea easy to follow, we use a deliberately simple scheme:
  1. POST /register  -> save a user with a hashed password
  2. POST /login      -> check the password, hand back a random token
  3. POST /courses    -> only works if you send that token in the header

This is simpler than real-world JWT auth, but it teaches the same core idea:
"you must prove who you are before you can access certain data."

Run with: uvicorn main:app --reload
Interactive docs at: http://127.0.0.1:8000/docs
"""
import hashlib
import secrets
from typing import List

from fastapi import Depends, FastAPI, Header, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Course Management API (with auth)")

# --- "Database" (in-memory, just like step 04) -----------------------------
users_db = {}          # email -> hashed_password
tokens_db = {}          # token -> email
courses_db = []         # list of course dicts


# --- Request/response shapes (Pydantic validates these automatically) ------
class UserRegister(BaseModel):
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class CourseCreate(BaseModel):
    name: str
    code: str
    credits: int


class CourseResponse(CourseCreate):
    id: int


# --- Helpers -----------------------------------------------------------------
def hash_password(password: str) -> str:
    """Never store plain-text passwords — always hash them first."""
    return hashlib.sha256(password.encode()).hexdigest()


def get_current_user(authorization: str = Header(...)) -> str:
    """
    Runs before any route that depends on it. Reads the `Authorization`
    header, checks the token is valid, and returns which user it belongs to.
    Raises 401 if the token is missing or wrong.
    """
    token = authorization.replace("Bearer ", "")
    email = tokens_db.get(token)
    if not email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing token",
        )
    return email


# --- Routes -------------------------------------------------------------------
@app.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: UserRegister):
    if user.email in users_db:
        raise HTTPException(status_code=409, detail="Email already registered")
    users_db[user.email] = hash_password(user.password)
    return {"message": "User registered successfully"}


@app.post("/login")
async def login(user: UserLogin):
    hashed = users_db.get(user.email)
    if not hashed or hashed != hash_password(user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Issue a random token and remember which user it belongs to.
    token = secrets.token_hex(16)
    tokens_db[token] = user.email
    return {"access_token": token, "token_type": "bearer"}


@app.get("/courses", response_model=List[CourseResponse])
async def list_courses():
    """Anyone can view courses — no login needed."""
    return courses_db


@app.post("/courses", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
async def create_course(course: CourseCreate, current_user: str = Depends(get_current_user)):
    """Only a logged-in user (valid token) can add a course."""
    new_course = CourseResponse(id=len(courses_db) + 1, **course.model_dump())
    courses_db.append(new_course.model_dump())
    return new_course
