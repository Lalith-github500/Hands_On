def validate_user(data):
    if "name" not in data or not data["name"]:
        raise ValueError("Name is required")

    if "age" not in data:
        raise ValueError("Age is required")

    if not isinstance(data["age"], int):
        raise ValueError("Age must be an integer")

    if data["age"] < 0:
        raise ValueError("Age must be non-negative")

    return True