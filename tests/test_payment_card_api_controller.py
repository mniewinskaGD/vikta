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

    def test_get_user_payment_card_by_id(self):
        get_card_response, get_card_data = self.verify_response_code(requests.get(self.payment_card_endpoint, params="id=48"), 200)
        self.assert_payment_card_api_controller_data(TestDataPaymentCardApiController.existing_payment_card_record, get_card_data)

    @pytest.mark.skip("500 error")
    def test_create_new_payment_card_record(self):
        pass

    def test_update_payment_card(self):
        payload = TestDataPaymentCardApiController.update_payment_card_record

        update_card_response, update_card_data = self.verify_response_code(requests.put(self.payment_card_endpoint, params="id=48", json=payload), 200)
        self.assert_payment_card_api_controller_data(payload, update_card_data)

        reverse_change_payload = TestDataPaymentCardApiController.existing_payment_card_record
        update_back_card_response, update_back_card_data = self.verify_response_code(requests.put(self.payment_card_endpoint, params="id=48", json=reverse_change_payload), 200)
        self.assert_payment_card_api_controller_data(reverse_change_payload, update_back_card_data)

    @pytest.mark.skip("There is only 1 record and I can create new")
    def test_delete_payment_card(self, create_test_user):
        pass

    def test_get_list_of_all_payment_card(self):
        get_card_list_response, data = self.verify_response_code(requests.get(self.payment_card_list_endpoint), 200)
        assert len(data) > 0

    @pytest.mark.skip("Search works in a way I don't understand")
    def test_get_payment_card_by_search_term(self):
        pass
