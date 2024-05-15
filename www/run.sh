#!/bin/bash

# Build Docker images
docker-compose build

# Start Docker containers
docker-compose up 

# Wait for containers to start
sleep 10

# Run Python script
python3 stimulate_server.py -a 172.20.0.2