#!/bin/bash

echo -ne "==> Running acceptance tests in open mode...\n"

$(npm run start:all) </dev/null &>/dev/null & \

source ./config/.env.local && \

# Wait for the CLIENT to be accessible
while ! nc -z localhost $CLIENT_PORT; do echo "==> Waiting on Client..." && sleep 3; done

cd acceptance && npm run cypress:open && \

echo -ne "==> Acceptance tests complete!\n"