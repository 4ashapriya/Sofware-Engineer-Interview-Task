import pytest
import requests
import json


url_server = "http://localhost:5000/"


def test_add_data():
    """ Test code for Upload Test data """
    url_login = url_server + "login"
    login_data = {"email": "asha@mail.com",
                    "password": "password"}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    login_response = requests.post(url_login, data=login_data, headers=headers)
    t = json.loads(login_response.text)
    header = {"x-access-token":t['token']}
    url_add_data = url_server + "add_data"
    data = 'static\Train.csv'
    response = requests.post(url_add_data, data=data, headers=header)
    print(f"test_AddData => {response}")
    assert response.status_code == 200
