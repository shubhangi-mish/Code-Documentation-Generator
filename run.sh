#!/bin/bash

echo "Running tests..."
pytest tests/

echo "Starting AI Documentation Generator..."
docker-compose up --build
