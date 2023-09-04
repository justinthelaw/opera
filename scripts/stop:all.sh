#!/bin/bash

wait_until_port_free() {
    local PORT=$1
    local RETRY_TIMES=30  # Adjust this as needed
    local SLEEP_TIME=1    # Adjust this as needed

    for ((i=0; i<$RETRY_TIMES; i++)); do
        # Check if port is occupied
        if ! nc -z localhost $PORT; then
            # Port is free, break out of loop
            return 0
        fi
        sleep $SLEEP_TIME
    done
    return 1  # If the loop completes, it means the port is still occupied
}

echo -ne "> Opera Development Environment is spinning down...\n"

# Source the environment file for checking
source ./config/.env.local

if nc -z localhost $CLIENT_PORT; then
    # Kill (gracefully, -15) the process using the client port
    kill -15 $(lsof -t -i :$CLIENT_PORT) >/dev/null 2>&1
    wait_until_port_free $CLIENT_PORT && \
    echo -ne "\r> Opera client has gracefully stopped.\n"
fi

if nc -z localhost $SERVER_PORT; then
    # Kill (gracefully, -15) the process using the server port
    kill -15 $(lsof -t -i :$SERVER_PORT) >/dev/null 2>&1
    wait_until_port_free $SERVER_PORT && \
    echo -ne "\r> Opera server has gracefully stopped.\n"
fi

if ! nc -z localhost $SERVER_PORT; then
    echo -ne "\r> Opera has gracefully stopped.\n"
fi


# Exit the script with a success status
exit 0
