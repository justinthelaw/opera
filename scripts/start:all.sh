#!/bin/bash

# Cleanup function to be called on SIGINT (Ctrl+C)
cleanup() {
    echo -ne "\r==> Running Smarter Bullets cleanup..."
    npm run stop:all
    # Exit the script with a success status
    exit 0
}

# Register the cleanup function to be called on SIGINT
trap cleanup SIGINT

echo "==> Smarter Bullets Development Environment is spinning up..."

npm run stop:all && \

# Source the environment file for checking
source ./config/.env.local && \

# Start the client with optional ":check" suffix
npm run start:client &
CLIENT_PID=$!

wait $CLIENT_PID
