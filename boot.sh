#!/bin/sh
# This script starts the app in the container
# (after its been installed)
export FLASK_APP=main.py
source venv/bin/activate
flask run --host=0.0.0.0