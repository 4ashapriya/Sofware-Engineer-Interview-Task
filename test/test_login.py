import pytest
import requests


url_server = "http://localhost:5000/"


def test_login():
    """ Test code for login """
    url_login = url_server + "login"
    data = {"email": "asha@mail.com",
            "password": "password"}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(url_login, data=data, headers=headers)
    print(f"test_Login => {response}")
    assert response.status_code == 201
