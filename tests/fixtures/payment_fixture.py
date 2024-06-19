import pytest
from tests.fixtures.base_fixtures import BaseTestAPIController, create_and_delete_resource, create_resource
from tests.test_data.test_data_payment_card_api_controller import TestDataPaymentCardApiController
from tests.test_payment_card_api_controller import TestPaymentCardAPIController


class TestPaymentCardAPIControllerFixture(BaseTestAPIController):
    endpoint = TestPaymentCardAPIController.payment_card_endpoint
    payload = TestDataPaymentCardApiController.base_payload



