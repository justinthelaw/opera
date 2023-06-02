#!/bin/bash

echo "==> Smarter Bullets Development Environment is spinning up...";

npm run install:all && source ./config/.env.local && \

if ! nc -z localhost $MONGO_PORT; then
    npm run start:database;
fi && \

if nc -z localhost $MONGO_PORT && ! nc -z localhost $API_PORT; then
    npm run start:api;
fi && \

if ! nc -z localhost $API_PORT && ! nc -z localhost $CLIENT_PORT; then
    npm run start:client;
fi && \

echo "==> Smarter Bullets Development Environment is up!";
echo "==> Logs for all sub-stacks will display below as they are written...";