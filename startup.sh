#!/bin/bash

# Run database migrations
flask db upgrade

# Populate the database with initial data
python scripts/populate_courses.py
python scripts/expanded_courses.py
python scripts/add_more_courses.py

# Start the application
gunicorn wsgi:app 