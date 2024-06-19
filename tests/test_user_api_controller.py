import pytest
import requests
from general.config import BASE_ENDPOINT
from general.test_assertion_helper import TestAssertionHelper
from general.test_base import TestBase
from tests.test_data.test_data_user_api_controller import TestDataUserAPIController


class TestUserAPIController(TestBase, TestAssertionHelper):
    user_endpoint = BASE_ENDPOINT + '/api/v1/user'
    user_list_endpoint = user_endpoint + '/list'
    user_login_endpoint = user_endpoint + '/login'
    user_search_endpoint = user_endpoint + '/search'
    user_surname_endpoint = user_endpoint + '/surname'

    @pytest.mark.parametrize("created_user, expected_response_code", [
        (({}, 0), 404),
        ("fixture", 200)])
    def test_get_user_record_by_id(self, created_user, expected_response_code, request):
        if created_user == "fixture":
            created_user = request.getfixturevalue("create_and_delete_test_user")

        created_user_data, created_user_user_id = created_user
        get_user_response, get_user_data = self.verify_response_code(requests.get(self.user_endpoint, params=f"id={created_user_user_id}"), expected_response_code)
        if expected_response_code == 200:
            self.assert_user_api_controller_data(created_user_data, get_user_data)

    @pytest.mark.parametrize("created_user_payload, expected_response_code", [
        (TestDataUserAPIController.base_payload, 201),
        (TestDataUserAPIController.generate_payload(email="a@b"), 201),
        (TestDataUserAPIController.generate_payload(email="email_without_at.com"), 500),
        (TestDataUserAPIController.generate_payload(email="a@"), 500)])
    def test_create_new_user(self, created_user_payload, expected_response_code):
        created_user_response, created_user_data = self.verify_response_code(requests.post(self.user_endpoint,
                                                                                           json=created_user_payload),
                                                                             expected_response_code)
        if expected_response_code == 201:
            user_id = created_user_data["id"]

            get_user_response, get_user_data = self.verify_response_code(requests.get(self.user_endpoint, params=f"id={user_id}"), 200)
            self.assert_user_api_controller_data(created_user_payload, get_user_data)

            requests.delete(TestUserAPIController.user_endpoint, params=f"id={user_id}")

    @pytest.mark.skip("500 error")
    @pytest.mark.usefixtures("create_and_delete_test_user")
    def test_update_user(self, create_and_delete_test_user):
        created_user_data, created_user_user_id = create_and_delete_test_user
        updated_payload = TestDataUserAPIController.generate_payload(id=created_user_user_id, loginName=created_user_data["loginName"])

        update_user_response, data = self.verify_response_code(requests.put(self.user_endpoint, json=updated_payload), 201)
        assert data == updated_payload
        assert created_user_user_id == data["id"]
        assert created_user_data["loginName"] == data["loginName"]

    @pytest.mark.usefixtures("create_test_user")
    def test_delete_user(self, create_test_user):
        created_user_data, created_user_user_id = create_test_user

        self.verify_response_code(requests.get(self.user_endpoint, params=f"id={created_user_user_id}"), 200)

        delete_user_response, delete_user_data = self.verify_response_code(requests.delete(self.user_endpoint, params=f"id={created_user_user_id}"), 200)
        assert delete_user_data["operationName"] == "Delete User"
        assert delete_user_data["statusMessage"] == f"SUCCESS,id= {created_user_user_id}"

        self.verify_response_code(requests.get(self.user_endpoint, params=f"id={created_user_user_id}"), 404)

    def test_get_list_of_all_users(self):
        get_user_list_response, data = self.verify_response_code(requests.get(self.user_list_endpoint), 200)
        assert len(data) > 0

    @pytest.mark.usefixtures("create_and_delete_test_user")
    def test_get_user_by_login_name(self, create_and_delete_test_user):
        created_user_data, created_user_user_id = create_and_delete_test_user
        login = created_user_data['loginName']
        _, data_by_login = self.verify_response_code(requests.get(self.user_login_endpoint, params=f"login={login}"),
                                                            200)
        _, data_by_user_id = self.verify_response_code(requests.get(self.user_endpoint, params=f"id={created_user_user_id}"),
                                                            200)
        assert data_by_login[0] == data_by_user_id

    def test_get_user_by_search_term(self):
        term = "City%7CTech%7Cservice%7Cadmin%7CTo4ka"
        user_id = 61
        _, data_by_search_term = self.verify_response_code(requests.get(self.user_search_endpoint, params=f"term={term}"),
                                                            200)
        _, data_by_user_id = self.verify_response_code(requests.get(self.user_endpoint, params=f"id={user_id}"),
                                                            200)
        assert data_by_search_term[0] == data_by_user_id

    @pytest.mark.usefixtures("create_and_delete_test_user")
    def test_get_user_by_surname(self, create_and_delete_test_user):
        created_user_data, created_user_user_id = create_and_delete_test_user
        surname = created_user_data['surname']
        _, data_by_surname = self.verify_response_code(requests.get(self.user_surname_endpoint, params=f"surname={surname}"),
                                                            200)
        _, data_by_user_id = self.verify_response_code(requests.get(self.user_endpoint, params=f"id={created_user_user_id}"),
                                                            200)
        assert data_by_surname[0] == data_by_user_id
