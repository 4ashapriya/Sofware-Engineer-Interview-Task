import pytest
import requests


url_server = "http://localhost:5000/"


def test_add_user():
    """ Test code for add_user """
    url_add_user = url_server + "add_user"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {"name": "Asha",
            "email": "asha@mail.com",
            "password": "password"}
    response = requests.post(url_add_user, data=data, headers=headers)
    print(f"test_AddUser => {response}")
    assert response.status_code == 201
