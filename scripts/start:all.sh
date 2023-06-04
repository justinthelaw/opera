#!/bin/bash

cleanup() {
    echo -e "\n==> Running Smarter Bullets cleanup..."
    if [[ $1 == "--check" ]]; then
        npm run stop:all:check
    else
        npm run stop:all
    fi
    exit 0
}

trap cleanup SIGINT

echo -e "\n==> Smarter Bullets Development Environment is spinning up..."

if [[ $1 == "--check" ]]; then
    source ./config/.env.example
else
    source ./config/.env.local
fi

npm run start:database &
database_pid=$!

while ! nc -z localhost $MONGO_PORT; do sleep 1; done

if [[ $1 == "--check" ]]; then
    npm run start:api:check &
    api_pid=$!
else
    npm run start:api &
    api_pid=$!
fi

while ! nc -z localhost $API_PORT; do sleep 1; done

npm run start:client &
client_pid=$!

if [[ $1 == "--check" ]]; then
    url="http://$CLIENT_HOST:$CLIENT_PORT"
    response=$(curl -s -o /dev/null -w "%{http_code}" "$url")

    while [[ $response -ne 200 ]]; do
        sleep 1
        response=$(curl -s -o /dev/null -w "%{http_code}" "$url")
    done

    echo -e "\n==> Performing final \"check:all\" cleanup..."
    cleanup
fi

wait $database_pid
wait $api_pid
wait $client_pid