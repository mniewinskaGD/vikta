import pytest


@pytest.mark.usefixtures("docker_fixture")
@pytest.mark.usefixtures("backend_is_responsive")
class TestBase:

    @staticmethod
    def verify_response_code(request, expected_code: int):
        response = request
        print(f"Request: {request.request.method} {request.url}")
        print(f"Response status code: {response.status_code}")
        print(f"Expected status code: {expected_code}")
        assert response.status_code == expected_code
        if expected_code == 500:
            data = {}
        else:
            data = response.json()
        return response, data
