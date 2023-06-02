#!/bin/bash

echo "==> Smarter Bullets Development Environment is spinning down..."

source ./config/.env.local

if nc -z localhost $MONGO_PORT; then
    docker stop mongodb >/dev/null 2>&1
fi && \
echo "==> Smarter Bullets Database has gracefully stopped."

if nc -z localhost $API_PORT; then
    kill -9 $(lsof -t -i :$API_PORT) >/dev/null 2>&1
fi && \
echo "==> Smarter Bullets API has gracefully stopped."

if nc -z localhost $CLIENT_PORT; then
    kill -9 $(lsof -t -i :$CLIENT_PORT) >/dev/null 2>&1
fi && \
echo "==> Smarter Bullets Client has gracefully stopped."

echo "==> All sub-stacks of Smarter Bullets have gracefully stopped."