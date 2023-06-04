#!/bin/bash

cleanup() {
    echo -ne "\r==> Running Smarter Bullets cleanup..."
    if [[ $1 == "--check" ]]; then
        npm run stop:all:check
    else
        npm run stop:all
    fi
    exit 0
}

trap cleanup SIGINT

echo -ne "==> Smarter Bullets Development Environment is spinning up..."

if [[ $1 == "--check" ]]; then
    source ./config/.env.example
else
    source ./config/.env.local

    npm run start:database &
    database_pid=$!

    while ! nc -z localhost $MONGO_PORT; do sleep 1; done
fi

npm run start:api${1:+:check} &
api_pid=$!

while ! nc -z localhost $API_PORT; do sleep 1; done

npm run start:client${1:+:check} &
client_pid=$!

if [[ $1 == "--check" ]]; then
    url="http://$CLIENT_HOST:$CLIENT_PORT"
    while true; do
        response=$(curl -s -o /dev/null -w "%{http_code}" "$url")
        [[ $response -eq 200 ]] && break
        sleep 1
    done

    echo -e "\r==> Performing final \"check:all\" cleanup..."
    cleanup --check
fi

if [[ $1 != "--check" ]]; then
    wait $database_pid
fi
wait $api_pid
wait $client_pid
