import uuid
import random
from datetime import datetime, timezone
from random_word import RandomWords


class TestDataImageItemApiController:
    current_datetime = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    randomization_str = str(uuid.uuid4()).replace("-", "")

    base_image_item = {
        "id": 0,
        "pathToImage": "https://miro.medium.com/max/812/1*jGgFf4dW7arnJocOKVN3Mw.jpeg",
        "title": f"{randomization_str[:10]}",
        "description": f"{RandomWords().get_random_word()}",
        "author": f"author_{randomization_str[10:15]}",
        "tags": [RandomWords().get_random_word()],
        "price": random.randint(1, 100),
        "rating": random.randint(1, 5),
        "categoryIds": [random.randint(1, 12)]
    }
