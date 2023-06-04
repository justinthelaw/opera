#!/bin/bash

echo -ne "==> Smarter Bullets Development Environment is spinning down...\n"

if [[ $1 == "--check" ]]; then
    source ./config/.env.example
else
    source ./config/.env.local
fi

if nc -z localhost $MONGO_PORT; then
    docker stop mongodb >/dev/null 2>&1 && \
    echo -ne "\r==> Smarter Bullets Database has gracefully stopped.\n"
fi && \

if nc -z localhost $API_PORT; then
    kill -9 $(lsof -t -i :$API_PORT) >/dev/null 2>&1 && \
    echo -ne "\r==> Smarter Bullets API has gracefully stopped.\n"
fi && \

if nc -z localhost $CLIENT_PORT; then
    kill -9 $(lsof -t -i :$CLIENT_PORT) >/dev/null 2>&1 && \
    echo -ne "\r==> Smarter Bullets Client has gracefully stopped.\n"
fi && \

sleep 1 && echo -ne "\r==> All sub-stacks of Smarter Bullets have gracefully stopped.\n" && \

exit 0