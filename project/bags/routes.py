from . import bags_blueprint
from flask import current_app, request
import flask
import json
from google.cloud import storage
from google.cloud.storage import Blob

@bags_blueprint.route('/')
@bags_blueprint.route('/index')
def index():
    return 'Welcome to the %s application. Please enjoy responsibly.' % (
        current_app.config.get('APP_NAME'))

@bags_blueprint.route('/scan', methods=['POST'])
def scan():
    rtn = {
        'scan': ''
    }
    if request.method == 'POST':
        # scan = json.loads(request.get_json())
        scan = request.get_json()
        rtn['scan'] = save_bag_scan(scan)
    return rtn

@bags_blueprint.route('/status')
@bags_blueprint.route('/status/<bag_id>')
def status(bag_id=None):
    """
        Return the last element for the specified bag
    """
    data_dict = get_bag_data(bag_id)
    rtn = ''
    if len(data_dict):
        rtn = json.dumps(data_dict[-1], indent=4)
    elif bag_id is not None:
        flask.abort(404)
    return rtn

@bags_blueprint.route('/history')
@bags_blueprint.route('/history/<bag_id>')
def history(bag_id=None):
    """
        Return all the elements for the specified bag
    """
    data_dict = get_bag_data(bag_id)
    rtn = ''
    if len(data_dict):
        rtn = json.dumps(data_dict, indent=4)
    elif bag_id is not None:
        flask.abort(404)
    return rtn

def get_bag_data(bag_id):
    """
        Retrieve the data from the storage bucket
        and then filter by the specified bag_id
    """
    storage_client = storage.Client()
    bucket_name = current_app.config.get('DATA_BUCKET_NAME')
    bucket = storage_client.get_bucket(bucket_name)
    fname = current_app.config.get('DATA_FILE_NAME')
    blob = Blob(fname, bucket)
    data_str = blob.download_as_string()
    data_dict = json.loads(data_str)
    if bag_id is None:
        bag_id = '000'
    rtn = []
    for data_item in data_dict:
        if data_item['bag'] == bag_id:
            rtn.append(data_item)
    return rtn

def save_bag_scan(scan):
    # Read in the file from GCP storage
    storage_client = storage.Client()
    bucket_name = current_app.config.get('DATA_BUCKET_NAME')
    bucket = storage_client.get_bucket(bucket_name)
    fname = current_app.config.get('DATA_FILE_NAME')
    blob = Blob(fname, bucket)
    data_str = blob.download_as_string()
    data_dict = json.loads(data_str)
    # Add record to end of data
    data_dict.append(scan)
    print(json.dumps(data_dict, indent=4))
    # Save the data back to GCP storage
    blob.upload_from_string(json.dumps(data_dict, indent=4))
    return len(data_dict)

