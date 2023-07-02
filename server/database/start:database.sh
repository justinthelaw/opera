#!/bin/bash

ENV=/config/.env.local
docker run --rm --name mongodb -v $PWD/server/database/db:/database/db -p $(awk -F "=" '/MONGO_PORT/{print $NF}' .$ENV):27017 --env-file $PWD/$ENV mongo:latest

