from api import fetch_user
from database import save_user


def process_user(user_id):
    user = fetch_user(user_id)

    if not user:
        raise ValueError("User not found")

    save_user(user)

    return f"User {user['name']} processed successfully"