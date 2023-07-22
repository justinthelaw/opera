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

echo "==> Opera Development Environment is spinning up..."

npm run stop:all && \

# Source the environment file for checking
source ./config/.env.local && \

# Start the client
npm run start:client &
CLIENT_PID=$!

# Start the server 
npm run start:server &
SERVER_PID=$!

wait $CLIENT_PID
wait $SERVER_PID
