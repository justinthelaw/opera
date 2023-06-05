#!/bin/bash

# This bash script spins up all subs-stacks of the application either in development (no flag) or check mode (--check)
# Check mode nulls the start of the database, as it assumes docker is working properly, and uses the correct .env fileß
# Note: docker cannot run inside the GitHub pipeline due to resource constraints

# Cleanup function to be called on SIGINT (Ctrl+C)
cleanup() {
    echo -ne "\r==> Running Smarter Bullets cleanup..."
    if [[ $1 == "--check" ]]; then
        npm run stop:all:check
    else
        npm run stop:all
    fi
    exit 0
}

# Register the cleanup function to be called on SIGINT
trap cleanup SIGINT

echo -ne "==> Smarter Bullets Development Environment is spinning up..."

if [[ $1 == "--check" ]]; then
    # Source the environment file for checking
    source ./config/.env.example
else
    # Source the local environment file
    source ./config/.env.local

    # Start the database in the background
    npm run start:database &
    database_pid=$!

    # Wait for the database to be accessible
    while ! nc -z localhost $MONGO_PORT; do sleep 1; done
fi

# Start the server with optional ":check" suffix
npm run start:server${1:+:check} &
server_pid=$!

# Wait for the server to be accessible
while ! nc -z localhost $SERVER_PORT; do sleep 1; done

# Start the client with optional ":check" suffix
npm run start:client${1:+:check} &
client_pid=$!

if [[ $1 == "--check" ]]; then
    url="http://$CLIENT_HOST:$CLIENT_PORT"
    while true; do
        # Check the HTTP response code
        response=$(curl -s -o /dev/null -w "%{http_code}" "$url")
        [[ $response -eq 200 ]] && break
        sleep 1
    done

    echo -e "\r==> Performing final \"check:all\" cleanup..."
    cleanup --check
fi

if [[ $1 != "--check" ]]; then
    # Wait for the database process to finish
    wait $database_pid
fi

# Wait for the server and client processes to finish
wait $server_pid
wait $client_pid
