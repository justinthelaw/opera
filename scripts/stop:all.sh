#!/bin/bash

echo -ne "==> Smarter Bullets Development Environment is spinning down...\n"

# Source the environment file for checking
source ./config/.env.local && \

if nc -z localhost $CLIENT_PORT; then
    # Kill (gracefully, -15) the process using the client port
    kill -15 $(lsof -t -i :$CLIENT_PORT) >/dev/null 2>&1 && \
    echo -ne "\r==> Smarter Bullets Client has gracefully stopped.\n"
fi && \

echo -ne "\r==> Smarter Bullets has gracefully stopped.\n" && \

# Exit the script with a success status
exit 0
