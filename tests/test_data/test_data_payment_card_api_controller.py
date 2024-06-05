import uuid
from datetime import datetime, timezone


class TestDataPaymentCardApiController:
    current_datetime = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    randomization_str = str(uuid.uuid4()).replace("-", "")
    randomization_number = str(uuid.uuid4().int)

    base_payment_card_record = {
        "id": 1,
        "cardNickName": f"firstName_{uuid.uuid4().hex}",
        "cardNumber": f"{randomization_number[:16]}",
        "cardCode": f"{randomization_number[:3]}",
        "ownerName": f"ownerName_{randomization_str[10:20]}",
        "expirationDate": f"{current_datetime}",
        "userId": 50
    }

    existing_payment_card_record = {
        "id": 47,
        "cardNickName": "Pod Del Ka",
        "cardNumber": "1228122112211431",
        "cardCode": "321",
        "ownerName": "BOYD BEATTY I",
        "expirationDate": "2013-9-12",
        "userId": 48
    }

    update_payment_card_record = {
        "id": 47,
        "cardNickName": f"cardNickName_{randomization_str[:10]}",
        "cardNumber": f"{randomization_number[:16]}",
        "cardCode": f"{uuid.uuid4().clock_seq_low}",
        "ownerName": f"ownerName_{randomization_str[10:20]}",
        "expirationDate": f"{current_datetime}",
        "userId": 48
    }
