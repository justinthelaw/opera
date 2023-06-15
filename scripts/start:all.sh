#!/bin/bash

# This bash script spins up all subs-stacks of the application either in development (no flag) or check mode (--check)
# Check mode nulls the start of the database, as it assumes docker is working properly, and uses the correct .env fileß
# Note: docker cannot run inside the GitHub pipeline due to resource constraints

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

# Start the database in the background
npm run start:database &
database_pid=$!

# Source the environment file for checking
source ./config/.env.local && \

# Wait for the database to be accessible
while ! nc -z localhost $MONGO_PORT; do sleep 1; done

# Start the server with optional ":check" suffix
npm run start:server${1:+:check} &
server_pid=$!

# Wait for the server to be accessible
while ! nc -z localhost $SERVER_PORT; do sleep 1; done

# Start the client with optional ":check" suffix
npm run start:client${1:+:check} &
client_pid=$!

# Wait for processes to finish
wait $database_pid
wait $server_pid
wait $client_pid
