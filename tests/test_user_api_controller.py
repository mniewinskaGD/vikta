import pytest
import requests
from general.config import BASE_ENDPOINT
from general.test_base import TestBase
from tests.test_data.test_data_user_api_controller import TestDataUserAPIController


class TestUserAPIController(TestBase):
    user_endpoint = BASE_ENDPOINT + '/api/v1/user'
    user_list_endpoint = user_endpoint + '/list'
    user_login_endpoint = user_endpoint + '/login'
    user_search_endpoint = user_endpoint + '/search'
    user_surname_endpoint = user_endpoint + '/surname'

    @pytest.mark.usefixtures("create_and_delete_test_user")
    def test_get_user_record_by_id(self, create_and_delete_test_user):
        data, user_id = create_and_delete_test_user
        get_user_response, data = self.verify_response_code(requests.get(self.user_endpoint, params=f"id={user_id}"), 200)
        assert data == TestDataUserAPIController.base_user_get

    def test_create_new_user(self):
        payload = TestDataUserAPIController.base_user_create

        create_user_response, data = self.verify_response_code(requests.post(self.user_endpoint, json=payload), 201)
        user_id = data["id"]

        get_user_response, get_user_data = self.verify_response_code(requests.get(self.user_endpoint, params=f"id={user_id}"), 200)
        assert get_user_data["email"] == payload["email"]
        assert get_user_data["firstName"] == payload["firstName"]
        assert get_user_data["loginName"] == payload["loginName"]
        assert get_user_data["middleName"] == payload["middleName"]
        assert get_user_data["password"] == payload["password"]
        assert get_user_data["paymentCardIds"] == payload["paymentCardIds"]
        assert get_user_data["surname"] == payload["surname"]
        assert get_user_data["pathToAvatarImage"] == payload["pathToAvatarImage"]

    @pytest.mark.skip("500 error")
    def test_update_user(self):
        payload = TestDataUserAPIController.updated_user_put

        update_user_response, data = self.verify_response_code(requests.put(self.user_endpoint, json=payload), 201)
        assert data == TestDataUserAPIController.base_user_get

    @pytest.mark.usefixtures("create_test_user")
    def test_delete_user(self, create_test_user):
        data, user_id = create_test_user

        self.verify_response_code(requests.get(self.user_endpoint, params=f"id={user_id}"), 200)

        delete_user_response, delete_user_data = self.verify_response_code(requests.delete(self.user_endpoint, params=f"id={user_id}"), 200)
        assert delete_user_data["operationName"] == "Delete User"
        assert delete_user_data["statusMessage"] == f"SUCCESS,id= {user_id}"

        get_user_response = requests.get(self.user_endpoint, params=f"id={user_id}")
        assert get_user_response.status_code == 404

    def test_get_list_of_all_users(self):
        get_user_list_response, data = self.verify_response_code(requests.get(self.user_list_endpoint), 200)
        assert len(data) > 0

    @pytest.mark.usefixtures("create_and_delete_test_user")
    def test_get_user_by_login_name(self, create_and_delete_test_user):
        data, user_id = create_and_delete_test_user
        login = data['loginName']
        _, data_by_login = self.verify_response_code(requests.get(self.user_login_endpoint, params=f"login={login}"),
                                                            200)
        _, data_by_user_id = self.verify_response_code(requests.get(self.user_endpoint, params=f"id={user_id}"),
                                                            200)
        assert data_by_login[0] == data_by_user_id

    def test_get_user_by_search_term(self):
        term = "City%7CTech%7Cservice%7Cadmin%7CTo4ka"
        user_id = 62
        _, data_by_surname = self.verify_response_code(requests.get(self.user_search_endpoint, params=f"term={term}"),
                                                            200)
        _, data_by_user_id = self.verify_response_code(requests.get(self.user_endpoint, params=f"id={user_id}"),
                                                            200)
        assert data_by_surname[0] == data_by_user_id

    @pytest.mark.usefixtures("create_and_delete_test_user")
    def test_get_user_by_surname(self, create_and_delete_test_user):
        data, user_id = create_and_delete_test_user
        surname = data['surname']
        _, data_by_surname = self.verify_response_code(requests.get(self.user_surname_endpoint, params=f"surname={surname}"),
                                                            200)
        _, data_by_user_id = self.verify_response_code(requests.get(self.user_endpoint, params=f"id={user_id}"),
                                                            200)
        assert data_by_surname[0] == data_by_user_id
