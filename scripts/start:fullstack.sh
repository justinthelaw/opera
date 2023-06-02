#!/bin/bash

# Function to execute when Ctrl+C is pressed
cleanup() {
    echo "==> Running Smarter Bullets cleanup..."
    npm run stop:fullstack
    exit 0
}

# Register the cleanup function to be called on SIGINT (Ctrl+C)
trap cleanup SIGINT

echo "==> Smarter Bullets Development Environment is spinning up..."

source ./config/.env.local

# Start the processes in the foreground
npm run start:database &
database_pid=$!

while ! nc -z localhost $MONGO_PORT; do sleep 1; done

npm run start:api &
api_pid=$!

while ! nc -z localhost $API_PORT; do sleep 1; done

npm run start:client &
client_pid=$!

# Wait for all processes to finish
wait $database_pid
wait $api_pid
wait $client_pid

echo "==> Smarter Bullets Development Environment is up and running!"
echo "==> Logs for all sub-stacks will display in this terminal as they are written."