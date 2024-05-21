import os

SERVICE_HOST = os.getenv("SERVICE_HOST", "localhost")
SERVICE_PORT = int(os.getenv("SERVICE_PORT", 5054))
BASE_ENDPOINT = f"http://{SERVICE_HOST}:{SERVICE_PORT}"
DOCKER_CONTAINER_NAME = "vikta"
DOCKER_IMAGE_NAME = "eng_qe-practice-dev/vikta:latest"