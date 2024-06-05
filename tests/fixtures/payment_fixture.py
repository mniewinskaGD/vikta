import pytest
from tests.fixtures.base_fixtures import BaseTestAPIController, create_and_delete_resource, create_resource
from tests.test_data.test_data_payment_card_api_controller import TestDataPaymentCardApiController
from tests.test_payment_card_api_controller import TestPaymentCardAPIController


class TestUserAPIControllerFixture(BaseTestAPIController):
    endpoint = TestPaymentCardAPIController.payment_card_endpoint
    payload = TestDataPaymentCardApiController.base_payment_card_record


@pytest.fixture
def create_and_delete_test_payment():
    yield from create_and_delete_resource(TestUserAPIControllerFixture)


@pytest.fixture
def create_test_payment():
    yield from create_resource(TestUserAPIControllerFixture)
