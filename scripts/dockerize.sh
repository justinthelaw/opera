#!/bin/bash

# Build Docker image
docker build --tag smarter-bullets-client ./

# Check if build succeeded
if [ $? -ne 0 ]; then
  echo "Error: Docker build failed"
  exit 1
fi

# Run Docker container
docker run --env-file ./config/.env.local --name smarter-bullets smarter-bullets-client

# Check if container is running
if [ ! "$(docker ps -q -f name=smarter-bullets)" ]; then
  echo "Error: Docker container failed to start"
  exit 1
fi

echo "Docker container is running"
