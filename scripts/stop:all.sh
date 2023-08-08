#!/bin/bash

echo -ne "> Opera Development Environment is spinning down...\n"

# Source the environment file for checking
source ./config/.env.local && \

if nc -z localhost $CLIENT_PORT; then
    # Kill (gracefully, -15) the process using the client port
    kill -15 $(lsof -t -i :$CLIENT_PORT) >/dev/null 2>&1 && \
    echo -ne "\r> Opera client has gracefully stopped.\n"
fi && \


if nc -z localhost $SERVER_PORT; then
    # Kill (gracefully, -15) the process using the client port
    kill -15 $(lsof -t -i :$SERVER_PORT) >/dev/null 2>&1 && \
    echo -ne "\r> Opera server has gracefully stopped.\n"
fi && \

if ! nc -z localhost $SERVER_PORT; then
    echo -ne "\r> Opera has gracefully stopped.\n"
fi && \

# Exit the script with a success status
exit 0
