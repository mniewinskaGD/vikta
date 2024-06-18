import uuid
import copy

from tests.test_data.base_test_data import BaseTestData


class TestDataUserAPIController(BaseTestData):
    base_user_create = {
        "addressIds": [],
        "email": f"email_{uuid.uuid4().hex}@a.com",
        "firstName": f"firstName_{uuid.uuid4().hex}",
        "id": 1,
        "loginName": f"loginName_{uuid.uuid4().hex}",
        "middleName": f"middleName_{uuid.uuid4().hex}",
        "password": f"{uuid.uuid4().hex}",
        "pathToAvatarImage": "",
        "paymentCardIds": [],
        "surname": f"surname_{uuid.uuid4().hex}"
    }

    updated_user_put = {
        "addressIds": [],
        "email": "b@b",
        "firstName": "b",
        "id": 50,
        "loginName": "b",
        "middleName": "b",
        "password": "456",
        "pathToAvatarImage": "https://5.imimg.com/data5/PM/TV/MY-44554651/baloon-decoration-500x500.jpg",
        "paymentCardIds": [],
        "surname": "b"
    }
