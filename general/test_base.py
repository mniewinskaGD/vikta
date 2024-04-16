import pytest


@pytest.mark.usefixtures("docker_fixture")
class TestBase:

    @staticmethod
    def verify_response_code(request, expected_code: int):
        response = request
        assert response.status_code == expected_code
        data = response.json()
        return response, data
