#
# This creates the application, and registers
# any Blueprints that it needs.
#
from flask import Flask
import json
from google.cloud import storage
from google.cloud.storage import Blob

# Create any global variables here

def create_app(config_filename=None):
    """
       Create the application and register Blueprints
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    initialize_extensions(app)
    register_blueprints(app)
    return app

def initialize_extensions(app):
    # Get the storage bucket
    storage_client = storage.Client()
    bucket_name = app.config.get('DATA_BUCKET_NAME')
    try:
        bucket = storage_client.get_bucket(bucket_name)
    except Exception as e:
        bucket = storage_client.create_bucket(bucket_name)
    # Test if the data file is found in the bucket, and
    # create it if it doesn't exist.
    blob = Blob(app.config.get('DATA_FILE_NAME'), bucket)
    if not blob.exists():
        # Open the initial data file
        init_fname = app.config.get('INIT_DATA_FILE')
        with open(init_fname) as infile:
            init_data = json.load(infile)
        # Copy it to the storage bucket
        blob.upload_from_string(json.dumps(init_data, indent=4))

def register_blueprints(app):
    from project.bags import bags_blueprint

    app.register_blueprint(bags_blueprint)