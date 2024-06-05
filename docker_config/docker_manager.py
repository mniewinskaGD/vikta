import time

import docker
import threading

from general.config import DOCKER_IMAGE_NAME, DOCKER_CONTAINER_NAME

"""
the Singleton pattern is used to ensure that only one instance of the DockerManager class is created
"""


class DockerManager:
    _instance = None  # to store the single instance of the class
    _lock = threading.Lock()  # to ensure that the instance creation is thread-safe

    def __new__(cls):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
                cls._instance.client = docker.from_env()
                cls._instance.container_name = DOCKER_CONTAINER_NAME
        return cls._instance

    def start_container(self):
        containers = self.get_containers()
        if containers:
            container = containers[0]
            if self.check_container_running(container):
                print("Docker container is already running.")
            else:
                print("Starting Docker container...")
                container.start()
                time.sleep(30)
        else:
            self.create_container()

    def stop_container(self):
        containers = self.client.containers.list(filters={"name": self.container_name})
        if containers:
            print("Stopping Docker container...")
            container = containers[0]
            container.stop()
        else:
            print("Docker container is not running.")

    def get_containers(self):
        containers = self.client.containers.list(all=True, filters={"name": self.container_name})
        return containers

    def check_container_running(self, container):
        return container.status == "running"

    def create_container(self):
        print("Creating Docker container...")
        self.client.containers.run(DOCKER_IMAGE_NAME, detach=True, name=self.container_name)
        time.sleep(30)
