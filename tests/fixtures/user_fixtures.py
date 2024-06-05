import pytest
from tests.fixtures.base_fixtures import BaseTestAPIController, create_and_delete_resource, create_resource
from tests.test_data.test_data_user_api_controller import TestDataUserAPIController
from tests.test_user_api_controller import TestUserAPIController


class TestUserAPIControllerFixture(BaseTestAPIController):
    endpoint = TestUserAPIController.user_endpoint
    payload = TestDataUserAPIController.base_user_create


@pytest.fixture
def create_and_delete_test_user():
    yield from create_and_delete_resource(TestUserAPIControllerFixture)


@pytest.fixture
def create_test_user():
    yield from create_resource(TestUserAPIControllerFixture)
