import time
import pytest
import requests

from general.config import BASE_ENDPOINT


@pytest.mark.usefixtures("docker_fixture")
class TestPageResponse:
    @pytest.mark.smoke
    @pytest.mark.parametrize("retry_count", [3, 5, 8])
    def test_page_response(self, retry_count):
        for _ in range(retry_count):
            response = requests.get(BASE_ENDPOINT)
            if response.status_code == 200:
                print("Page responded 200 OK")
                break
            else:
                time.sleep(2)
        else:
            assert False, f"Page did not return 200 after {retry_count} retries"
