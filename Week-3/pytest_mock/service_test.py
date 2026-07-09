from unittest.mock import patch
from service import process_user
import pytest


@patch("service.save_user")
@patch("service.fetch_user")
def test_process_user_success(mock_fetch_user, mock_save_user):
    mock_fetch_user.return_value = {
        "id": 1,
        "name": "Alice"
    }

    result = process_user(1)

    mock_fetch_user.assert_called_once_with(1)
    mock_save_user.assert_called_once_with({
        "id": 1,
        "name": "Alice"
    })

    assert result == "User Alice processed successfully"


@patch("service.fetch_user")
def test_process_user_not_found(mock_fetch_user):
    mock_fetch_user.return_value = None

    with pytest.raises(ValueError, match="User not found"):
        process_user(1)