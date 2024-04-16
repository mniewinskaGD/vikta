import pytest

from docker_config.docker_manager import DockerManager


@pytest.fixture(scope='session')
def docker_fixture() -> DockerManager:
    docker_manager = DockerManager()
    docker_manager.start_container()
    yield docker_manager
    docker_manager.stop_container()




