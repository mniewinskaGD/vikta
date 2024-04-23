import pytest

from docker_config.docker_manager import DockerManager


@pytest.fixture(scope='session')
def docker_fixture():
    docker_manager = DockerManager()
    docker_manager.start_container()
    yield docker_manager
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


