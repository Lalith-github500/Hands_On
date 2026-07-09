import pytest
from validator import validate_user


def test_valid_user():
    assert validate_user({
        "name": "Alice",
        "age": 25
    }) is True


def test_missing_name():
    with pytest.raises(ValueError, match="Name is required"):
        validate_user({
            "age": 25
        })


def test_empty_name():
    with pytest.raises(ValueError, match="Name is required"):
        validate_user({
            "name": "",
            "age": 25
        })


def test_missing_age():
    with pytest.raises(ValueError, match="Age is required"):
        validate_user({
            "name": "Alice"
        })


def test_age_not_integer():
    with pytest.raises(ValueError, match="Age must be an integer"):
        validate_user({
            "name": "Alice",
            "age": "25"
        })


def test_negative_age():
    with pytest.raises(ValueError, match="Age must be non-negative"):
        validate_user({
            "name": "Alice",
            "age": -1
        })