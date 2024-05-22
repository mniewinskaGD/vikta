import time

import pytest
import requests
from general.config import BASE_ENDPOINT
from docker_config.docker_manager import DockerManager


def pytest_addoption(parser):
    parser.addoption('--stop_docker_container', action='store', default=False)


@pytest.fixture(scope='session')
def docker_fixture(request):
    docker_manager = DockerManager()
    docker_manager.start_container()
    yield docker_manager
    if request.config.option.stop_docker_container:
        docker_manager.stop_container()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    # customize the report
    outcome = yield
    report = outcome.get_result()
    test_fn = item.obj

    params = item.callspec.params if hasattr(item, 'callspec') else {}
    descr_marker = item.get_closest_marker('description')
    test_title = getattr(test_fn, '__doc__')

    if test_title:
        report.test_title = test_title

    if descr_marker:
        text = descr_marker.kwargs.get('text', '')
        report.test_title = text.format(**params)


@pytest.fixture(scope="session")
def backend_is_responsive():
    retry_count = 3
    for _ in range(retry_count):
        response = requests.get(BASE_ENDPOINT)
        if response.status_code == 200:
            break
        else:
            time.sleep(2)
    else:
        assert False, f"Page did not return 200 after {retry_count} retries"
