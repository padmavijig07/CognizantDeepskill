from unittest.mock import patch
import requests

def get_user():
    return {
        "id": 1,
        "name": "Mokitha"
    }

def get_status():
    response = requests.get("https://example.com")
    return response.status_code

@patch("__main__.get_user")
def test_database(mock_db):
    mock_db.return_value = {
        "id": 2,
        "name": "Rahul"
    }

    user = get_user()
    print("Database:", user)

@patch("requests.get")
def test_http(mock_get):
    mock_get.return_value.status_code = 200
    print("HTTP Status:", get_status())

if __name__ == "__main__":
    test_database()
    test_http()

