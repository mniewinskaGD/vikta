# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.10
FROM python:${PYTHON_VERSION}-slim as base

# Install Docker CLI
RUN apt-get update && \
    apt-get install -y docker.io

# Copy the requirements file into the container
COPY requirements.txt /requirements.txt

# Install any dependencies
RUN pip install -r /requirements.txt

# Copy pytest configuration
COPY pytest.ini /pytest.ini

# Run the application.
CMD /bin/bash
