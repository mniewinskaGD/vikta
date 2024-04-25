import pytest


@pytest.mark.usefixtures("docker_fixture")
@pytest.mark.usefixtures("backend_is_responsive")
class TestBase:

    @staticmethod
    def verify_response_code(request, expected_code: int):
        response = request
        assert response.status_code == expected_code
        data = response.json()
        print(f"Request: {request.url}")
        print(f"Response status code: {response.status_code}")
        return response, data
