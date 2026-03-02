#!/bin/bash

PROJECT_NAME="smart-llm-router"

echo "Creating project structure..."

mkdir -p $PROJECT_NAME/app
mkdir -p $PROJECT_NAME/data/raw
mkdir -p $PROJECT_NAME/data/processed
mkdir -p $PROJECT_NAME/models
mkdir -p $PROJECT_NAME/logs
mkdir -p $PROJECT_NAME/notebooks
mkdir -p $PROJECT_NAME/tests

touch $PROJECT_NAME/app/__init__.py
touch $PROJECT_NAME/app/main.py
touch $PROJECT_NAME/app/router.py
touch $PROJECT_NAME/app/complexity.py
touch $PROJECT_NAME/app/models.py
touch $PROJECT_NAME/app/fallback.py
touch $PROJECT_NAME/app/cost.py
touch $PROJECT_NAME/app/config.py

touch $PROJECT_NAME/requirements.txt
touch $PROJECT_NAME/README.md
touch $PROJECT_NAME/run.sh

echo "Project structure created successfully."
