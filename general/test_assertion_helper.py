class TestAssertionHelper:

    @staticmethod
    def assert_data(expected_data, observed_data, keys, data_type):
        print(f"Compare all fields of {data_type} data")
        for key in keys:
            assert expected_data[key] == observed_data[key], f"Mismatch in {key}: expected {expected_data[key]}, got {observed_data[key]}"

    @staticmethod
    def assert_user_api_controller_data(expected_data, observed_data):
        user_keys = ["email", "addressIds", "firstName", "loginName", "middleName", "password", "paymentCardIds", "surname"]
        TestAssertionHelper.assert_data(expected_data, observed_data, user_keys, "user API controller")

    @staticmethod
    def assert_payment_card_api_controller_data(expected_data, observed_data):
        card_keys = ["cardNickName", "cardNumber", "cardCode", "ownerName", "expirationDate", "userId"]
        TestAssertionHelper.assert_data(expected_data, observed_data, card_keys, "payment card API controller")