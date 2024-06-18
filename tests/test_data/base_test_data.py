import copy


class BaseTestData:
    base_payload = {}

    @classmethod
    def generate_payload(cls, **kwargs):
        payload = copy.deepcopy(cls.base_payload)
        payload.update(kwargs)
        return payload
