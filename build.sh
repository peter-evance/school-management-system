#!/bin/bash

# This script is used to build and set up the Django project.

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade pip to the latest version
pip install --upgrade pip

# Install project dependencies
if ! pip install -r /vercel/path0/requirements.txt; then
  echo "Error: Failed to install dependencies."
  exit 1
fi

# Make database migrations
if ! python /vercel/path0/manage.py makemigrations core; then
  echo "Error: Failed to make migrations for core app."
  exit 1
fi

if ! python /vercel/path0/manage.py makemigrations users; then
  echo "Error: Failed to make migrations for users app."
  exit 1
fi

if ! python /vercel/path0/manage.py migrate; then
  echo "Error: Failed to apply migrations."
  exit 1
fi

# Minimal handler function to satisfy Vercel requirements
handler() {
  echo "Vercel deployment complete."
}
