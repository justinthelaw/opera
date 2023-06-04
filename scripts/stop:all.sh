#!/bin/bash

echo -e "\n==> Smarter Bullets Development Environment is spinning down...\n"

source ./config/.env.local

if nc -z localhost $MONGO_PORT; then
    docker stop mongodb >/dev/null 2>&1 && \
    echo "==> Smarter Bullets Database has gracefully stopped."
fi && \

if nc -z localhost $API_PORT; then
    kill -9 $(lsof -t -i :$API_PORT) >/dev/null 2>&1 && \
    echo "==> Smarter Bullets API has gracefully stopped."
fi && \

if nc -z localhost $CLIENT_PORT; then
    kill -9 $(lsof -t -i :$CLIENT_PORT) >/dev/null 2>&1 && \
    echo "==> Smarter Bullets Client has gracefully stopped."
fi && \

sleep 3 && echo -e "\n==> All sub-stacks of Smarter Bullets have gracefully stopped." && \

exit 0