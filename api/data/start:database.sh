#!/bin/bash

if [[ $1 == "--check" ]]; then
    ENV=/config/.env.example
else
    ENV=/config/.env.local
fi

docker run --rm --name mongodb -v $PWD/api/data/db:/data/db -p $(awk -F "=" '/MONGO_PORT/{print $NF}' .$ENV):27017 --env-file $PWD/$ENV mongodb/mongodb-community-server:latest