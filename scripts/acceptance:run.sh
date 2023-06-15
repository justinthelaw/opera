#!/bin/bash

# This bash script spins up all subs-stacks of the application and runs the
# cypress (acceptance) tests in closed/headless mode

echo -ne "==> Running acceptance tests in headless mode...\n"

$(npm run start:all) </dev/null &>/dev/null & \

source ./config/.env.local && \

# Wait for the database to be accessible
while ! nc -z localhost $MONGO_PORT; do echo "==> Waiting on Database..." && sleep 1; done
# Wait for the server to be accessible
while ! nc -z localhost $SERVER_PORT; do echo "==> Waiting on Server..." && sleep 1; done
# Wait for the CLIENT to be accessible
while ! nc -z localhost $CLIENT_PORT; do echo "==> Waiting on Client..." && sleep 1; done

cd acceptance && npm run cypress:run && \

echo -ne "==> Acceptance tests complete!\n"