import pytest
import requests


@pytest.mark.usefixtures("restart_api")
def test_authors() -> None:
    request = requests.get("http://backend_test:8000/authors")

    assert request.status_code == 200


@pytest.mark.usefixtures("restart_api")
def test_create_author() -> None:
    data = {
            "fullname": {
                "first_name": "str",
                "last_name": "str",
            },
            "biography": "",
    }
    request = requests.post("http://backend_test:8000/authors", json=data)

    assert request.status_code == 201
    assert request.json()["created"]["fullname"]["first_name"] == data["fullname"]["first_name"]

