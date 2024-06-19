import uuid
from datetime import datetime, timezone

from tests.test_data.base_test_data import BaseTestData


class TestDataPaymentCardApiController(BaseTestData):
    current_datetime = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    randomization_str = str(uuid.uuid4()).replace("-", "")
    randomization_number = str(uuid.uuid4().int)

    base_payload = {
        "id": 1,
        "cardNickName": f"firstName_{uuid.uuid4().hex}",
        "cardNumber": f"{randomization_number[:16]}",
        "cardCode": f"{randomization_number[:3]}",
        "ownerName": f"ownerName_{randomization_str[10:20]}",
        "expirationDate": f"{current_datetime}",
        "userId": 50
    }

