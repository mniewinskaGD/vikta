import pytest
import requests
from tests.test_data.test_data_user_api_controller import TestDataUserAPIController
from tests.test_user_api_controller import TestUserAPIController


@pytest.fixture
def create_and_delete_test_user(create_test_user):
    data, user_id = create_test_user
    yield data, user_id
    requests.delete(TestUserAPIController.user_endpoint, params=f"id={user_id}")


@pytest.fixture
def create_test_user():
    payload = TestDataUserAPIController.base_user_create
    create_user_response = requests.post(TestUserAPIController.user_endpoint, json=payload)
    data = create_user_response.json()
    user_id = data["id"]
    yield data, user_id