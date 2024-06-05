# Use the official Jenkins image as the base image
FROM jenkins/jenkins:lts

# Switch to root user to install packages
USER root


# Install Python and any other dependencies
RUN apt-get update --fix-missing && \
    apt-get install -y -y python3 python3-venv python3-pip docker.io && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Switch back to the jenkins user
USER jenkins
