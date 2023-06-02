#!/bin/bash

docker run --rm --name mongodb -v $PWD/server/data/db:/data/db -p $(awk -F "=" '/MONGO_PORT/{print $NF}' ./config/.env.local):27017 --env-file $PWD/config/.env.local mongodb/mongodb-community-server:latest