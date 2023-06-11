#!/bin/bash

# Similar to the start:all command, this script ends the entire sub-stack based on
# development (no flag) or the check (--check) flag
# Check mode uses the correct .env file

echo -ne "==> Smarter Bullets Development Environment is spinning down...\n"

if [[ $1 == "--check" ]]; then
    # Source the environment file for checking
    source ./config/.env.example
else
    # Source the local environment file
    source ./config/.env.local
fi

if nc -z localhost $MONGO_PORT; then
    # Stop MongoDB gracefully
    docker stop mongodb >/dev/null 2>&1 && \
    echo -ne "\r==> Smarter Bullets Database has gracefully stopped.\n"
fi && \

if nc -z localhost $SERVER_PORT; then
    # Kill (gracefully, -15) the process using the server port
    kill -15 $(lsof -t -i :$SERVER_PORT) >/dev/null 2>&1 && \
    echo -ne "\r==> Smarter Bullets server has gracefully stopped.\n"
fi && \

if nc -z localhost $CLIENT_PORT; then
    # Kill (gracefully, -15) the process using the client port
    kill -15 $(lsof -t -i :$CLIENT_PORT) >/dev/null 2>&1 && \
    echo -ne "\r==> Smarter Bullets Client has gracefully stopped.\n"
fi && \

echo -ne "\r==> All sub-stacks of Smarter Bullets have gracefully stopped.\n" && \

# Exit the script with a success status
exit 0
