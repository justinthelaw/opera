#!/bin/bash

ENV=/config/.env.local
docker run --rm --name mongodb -v $PWD/server/data/db:/data/db -p $(awk -F "=" '/MONGO_PORT/{print $NF}' .$ENV):27017 --env-file $PWD/$ENV mongodb/mongodb-community-server:latest

