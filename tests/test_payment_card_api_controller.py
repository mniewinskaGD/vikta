import pytest
import requests
from general.config import BASE_ENDPOINT
from general.test_assertion_helper import TestAssertionHelper
from general.test_base import TestBase
from tests.test_data.test_data_payment_card_api_controller import TestDataPaymentCardApiController


class TestPaymentCardAPIController(TestBase, TestAssertionHelper):
    payment_card_endpoint = BASE_ENDPOINT + '/api/v1/paymentcard'
    payment_card_list_endpoint = payment_card_endpoint + '/list'
    payment_card_search_endpoint = payment_card_endpoint + '/search'

    @pytest.mark.usefixtures("create_and_delete_test_payment")
    def test_get_user_payment_card_by_id(self, create_and_delete_test_payment):
        created_payment_data, created_payment_id = create_and_delete_test_payment
        get_card_response, get_card_data = self.verify_response_code(
            requests.get(self.payment_card_endpoint, params=f"id={created_payment_id}"), 200)
        self.assert_payment_card_api_controller_data(created_payment_data, get_card_data)

    def test_create_new_payment_card_record(self):
        payload = TestDataPaymentCardApiController.base_payment_card_record

        created_payment_response, created_payment_data = self.verify_response_code(
            requests.post(self.payment_card_endpoint, json=payload), 201)
        payment_id = created_payment_data["id"]

        get_payment_response, get_payment_data = self.verify_response_code(
            requests.get(self.payment_card_endpoint, params=f"id={payment_id}"), 200)
        self.assert_payment_card_api_controller_data(payload, get_payment_data)

        requests.delete(TestPaymentCardAPIController.payment_card_endpoint, params=f"id={payment_id}")

    @pytest.mark.usefixtures("create_test_payment")
    def test_update_payment_card(self, create_test_payment):
        created_payment_data, created_payment_id = create_test_payment
        payload = TestDataPaymentCardApiController.update_payment_card_record

        update_card_response, update_card_data = self.verify_response_code(
            requests.put(self.payment_card_endpoint, params=f"id={created_payment_id}", json=payload), 200)
        self.assert_payment_card_api_controller_data(payload, update_card_data)

    @pytest.mark.usefixtures("create_test_payment")
    def test_delete_payment_card(self, create_test_payment):
        created_payment_data, created_payment_id = create_test_payment

        self.verify_response_code(requests.get(self.payment_card_endpoint, params=f"id={created_payment_id}"), 200)

        delete_user_response, delete_user_data = self.verify_response_code(
            requests.delete(self.payment_card_endpoint, params=f"id={created_payment_id}"), 200)
        assert delete_user_data["operationName"] == "Delete PaymentCard"
        assert delete_user_data["statusMessage"] == f"SUCCESS,id= {created_payment_id}"

        self.verify_response_code(requests.get(self.payment_card_endpoint, params=f"id={created_payment_id}"), 404)

    def test_get_list_of_all_payment_card(self):
        get_card_list_response, data = self.verify_response_code(requests.get(self.payment_card_list_endpoint), 200)
        assert len(data) > 0

    @pytest.mark.skip("Search works in a way I don't understand")
    def test_get_payment_card_by_search_term(self):
        pass
