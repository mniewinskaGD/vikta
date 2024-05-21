
class TestAssertionHelper:

    @staticmethod
    def assert_user_api_controller_data(expected_data, observed_data):
        assert expected_data["email"] == observed_data["email"]
        assert expected_data["addressIds"] == observed_data["addressIds"]
        assert expected_data["firstName"] == observed_data["firstName"]
        assert expected_data["loginName"] == observed_data["loginName"]
        assert expected_data["middleName"] == observed_data["middleName"]
        assert expected_data["password"] == observed_data["password"]
        assert expected_data["paymentCardIds"] == observed_data["paymentCardIds"]
        assert expected_data["surname"] == observed_data["surname"]
    @staticmethod
    def assert_payment_card_api_controller_data(expected_data, observed_data):
        assert expected_data["cardNickName"] == observed_data["cardNickName"]
        assert expected_data["cardNumber"] == observed_data["cardNumber"]
        assert expected_data["cardCode"] == observed_data["cardCode"]
        assert expected_data["ownerName"] == observed_data["ownerName"]
        assert expected_data["expirationDate"] == observed_data["expirationDate"]
        assert expected_data["userId"] == observed_data["userId"]