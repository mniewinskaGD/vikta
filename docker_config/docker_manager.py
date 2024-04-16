import docker
import threading


class DockerManager:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
                cls._instance.client = docker.from_env()
                cls._instance.container_name = "vikta"
        return cls._instance

    def check_container_existence(self):
        containers = self.client.containers.list(filters={"name": self.container_name})
        return len(containers) > 0

    def check_container_running(self):
        containers = self.client.containers.list(filters={"name": self.container_name})
        if containers:
            container = containers[0]
            return container.status == "running"
        return False

    def create_container(self):
        if not self.check_container_existence():
            print("Creating Docker container...")
            self.client.containers.run("your_image_name", detach=True, name=self.container_name)
        else:
            print("Docker container already exists.")

    def start_container(self):
        if not self.check_container_running():
            print("Starting Docker container...")
            containers = self.client.containers.list(filters={"name": self.container_name})
            if containers:
                container = containers[0]
                container.start()
        else:
            print("Docker container is already running.")

    def stop_container(self):
        containers = self.client.containers.list(filters={"name": self.container_name})
        if containers:
            print("Stopping Docker container...")
            container = containers[0]
            container.stop()
        else:
            print("Docker container is not running.")


