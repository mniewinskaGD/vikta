class TestDataUserAPIController:
    base_user_create = {
        "addressIds": [
            0
        ],
        "email": "a@a",
        "firstName": "a",
        "id": 0,
        "loginName": "a",
        "middleName": "a",
        "password": "123",
        "pathToAvatarImage": "string",
        "paymentCardIds": [
            0
        ],
        "surname": "a"
    }
    base_user_get = {
        "id": 63,
        "loginName": "a",
        "password": "123",
        "email": "a@a",
        "firstName": "a",
        "middleName": "a",
        "surname": "a",
        "pathToAvatarImage": "http://lorempixel.com/640/480/transport/",
        "addressIds": [],
        "paymentCardIds": []
    }
    updated_user_put = {
        "addressIds": [
            0
        ],
        "email": "b@b",
        "firstName": "b",
        "id": 64,
        "loginName": "b",
        "middleName": "b",
        "password": "456",
        "pathToAvatarImage": "http://lorempixel.com/640/480/transport/",
        "paymentCardIds": [
            0
        ],
        "surname": "b"
    }
