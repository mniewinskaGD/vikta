import uuid
from datetime import datetime, timezone


class TestDataPaymentCardApiController:
    current_datetime = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    randomization_str = str(uuid.uuid4()).replace("-", "")
    randomization_number = str(uuid.uuid4().int)

    existing_payment_card_record = {
        "id": 48,
        "cardNickName": "Pod Del Ka",
        "cardNumber": "1234212112211211",
        "cardCode": "321",
        "ownerName": "JARRETT GERLACH",
        "expirationDate": "2012-11-12",
        "userId": 49
    }

    update_payment_card_record = {
        "id": 48,
        "cardNickName": f"cardNickName_{randomization_str[:10]}",
        "cardNumber": f"{randomization_number[:16]}",
        "cardCode": f"{uuid.uuid4().clock_seq_low}",
        "ownerName": f"ownerName_{randomization_str[10:20]}",
        "expirationDate": f"{current_datetime}",
        "userId": 49
    }
