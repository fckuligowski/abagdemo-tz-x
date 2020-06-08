#!/bin/sh
# This script starts the app in the container
# (after its been installed)
#export MODE=$1
echo "The mode variable is: $MODE"
if [ "$MODE" = "TESTING" ]; then
    export PYTHONPATH=`pwd`
    source venv/bin/activate
    pytest --setup-show
else
    export FLASK_APP=main.py
    source venv/bin/activate
    flask run --host=0.0.0.0
fi    
# Use these commands if you want to create this as a
# keep-alive container, so you can see what files are there.
#env
#tail -f /dev/null