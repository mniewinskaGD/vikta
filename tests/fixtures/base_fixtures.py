import requests
"""
Factory Method: Create a generic function to handle the creation and deletion of resources.
Template Method: Define a base class that includes the template methods for creation and deletion,
and then subclass it for each specific resource type.
"""


class BaseTestAPIController:
    endpoint = ""
    payload = {}

    @classmethod
    def create(cls):
        response = requests.post(cls.endpoint, json=cls.payload)
        data = response.json()
        return data, data["id"]

    @classmethod
    def delete(cls, resource_id):
        requests.delete(cls.endpoint, params=f"id={resource_id}")


def create_and_delete_resource(resource_controller):
    data, resource_id = resource_controller.create()
    print(f"Create resource\n id:{resource_id}")
    yield data, resource_id
    resource_controller.delete(resource_id)
    print(f"Deleted resource\n id: {resource_id}")


def create_resource(resource_controller):
    data, resource_id = resource_controller.create()
    print(f"Create resource\n id:{resource_id}")
    yield data, resource_id

