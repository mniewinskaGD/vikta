import re
import time

import pytest
import requests
from general.config import BASE_ENDPOINT
from docker_config.docker_manager import DockerManager


def pytest_addoption(parser):
    parser.addoption('--stop_docker_container', action='store', default=False)
    parser.addoption("--test_report", action="store", default=None,
                     help="Generate HTML report and store it in the specified file")


@pytest.fixture(scope='class')
def docker_fixture(request):
    docker_manager = DockerManager()
    print(docker_manager)
    docker_manager.start_container()
    yield docker_manager
    if request.config.option.stop_docker_container:
        docker_manager.stop_container()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    # customize the report
    outcome = yield
    report = outcome.get_result()

    params = item.callspec.params if hasattr(item, 'callspec') else {}
    descr_marker = item.get_closest_marker('description')

    if descr_marker:
        text = descr_marker.kwargs.get('text', '')
        report.test_title = text.format(**params)

@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_row(report, cells):
    for cell in cells:
        if cell.attr.class_ == 'col-name':
            if hasattr(report, 'test_title'):
                cell[0] = report.test_title
            break


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


def pytest_configure(config):
    test_report = config.getoption("--test_report")
    if test_report:
        config.option.htmlpath = test_report
        config.option.self_contained_html = True
