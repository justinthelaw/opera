#!/bin/bash

# Cleanup function to be called on SIGINT (Ctrl+C)
cleanup() {
    echo -ne "\r==> Running Opera cleanup..."
    npm run stop:all
    # Exit the script with a success status
    exit 0
}

# Register the cleanup function to be called on SIGINT
trap cleanup SIGINT

echo -ne "==> Running acceptance tests in headless mode...\n"

$(npm run start:all) </dev/null &>/dev/null & \

source ./config/.env.local && \

# Wait for the CLIENT to be accessible
while ! nc -z localhost $CLIENT_PORT; do echo "==> Waiting on Client..." && sleep 3; done

cd acceptance && npm run cypress:run && \ 

cd ../ && npm run stop:all && \

echo -ne "==> Acceptance tests complete!\n"