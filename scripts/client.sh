#!/bin/bash

# install dependencies
cd ../client && npm install

# build docker image
docker build --tag smarter-bullets-client ./

# check if build succeeded
if [ $? -ne 0 ]; then
  echo "Error: smarter-bullets-client build failed"
  exit 1
fi

# run docker container
docker run --env-file ./config/.env.local --name smarter-bullets smarter-bullets-client

# check if container is running
if [ ! "$(docker ps -q -f name=smarter-bullets)" ]; then
  echo "Error: smarter-bullets-client failed to start"
  exit 1
fi

echo "smarter-bullets-client container is running"
