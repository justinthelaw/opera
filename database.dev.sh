#!/bin/bash

docker run --rm --name smarter-bullets -v $PWD:/docker-entrypoint-initdb.d/ --env-file $PWD/config/.env.local -p $(awk -F "=" '/PG_PORT/{print $NF}' ./config/.env.local):5432 postgres:latest