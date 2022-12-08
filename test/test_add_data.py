import pytest
import requests


url_server = "http://localhost:5000/"


def test_add_data():
    """ Test code for Upload Test data """
    url_add_data = url_server + "add_data"
    data = 'static\Train.csv'
    header = {"x-access-token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiI4OWNlNzg3Mi1hYjcxLTRkNDAtYmNhNy0wOThjNjJkMGZkYzYiLCJleHAiOjE2NzA1Mzg0MDN9.DmJFlCk0jOlKwSmCA-q0FqtAPqqwxUQ3ZvStOEW8Rxs"}
    response = requests.post(url_add_data, data=data, headers=header)
    print(f"test_AddData => {response}")
    assert response.status_code == 200