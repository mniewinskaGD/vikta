import uuid

from tests.test_data.base_test_data import BaseTestData


class TestDataUserAPIController(BaseTestData):
    base_payload = {
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

