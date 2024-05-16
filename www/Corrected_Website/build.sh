#!/bin/bash

docker-compose down

sleep(10)

# Build Docker images
docker-compose build

# Start Docker containers
docker-compose up 