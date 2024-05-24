#!/bin/bash

: '
.SYNOPSIS
Runs a Docker container with specified configurations.

.DESCRIPTION
This script runs udp-qa-framework container with the following configurations:
- Interactive mode (-it)
- Port mapping 8080:8080
- Volume mapping from framework base directory to container /test directory
- Working directory set to container /test directory
'

host_dir=$(dirname $(pwd))
container_dir=/vikta

docker run \
  -it \
  -p 6060:6060 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v "$host_dir":"$container_dir" \
  -w "$container_dir" \
  -e SERVICE_HOST=host.docker.internal \
  -e SERVICE_PORT=5054 \
  vikta-framework:latest
