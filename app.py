from flask import Blueprint
from flask import jsonify
import boto3
from flask import send_file

bp = Blueprint('aws_iam', __name__)

from flask import Flask

app = Flask(__name__)

@app.route('/list-users/', methods = ['GET'])
def get_all_users():
    client = boto3.client('iam')
    users = client.list_users().get('Users', [])

    if len(users) == 0:
        return {}

    return {'users': [obj['UserName'] for obj in users]}

@app.route('/users/<string:username>/tags/', methods=['GET'])
def get_user_tags(username):
    client = boto3.client('iam')
    try:
        user_tags = client.list_user_tags(
            UserName = username
        ).get('Tags', [])
    except Exception as ex:
        return jsonify(error="user not found"), 404
    return {'tags': user_tags}

@app.route('/users/<string:username>/access-key-details/', methods=['GET'])
def get_user_access_key_details(username):
    client = boto3.client('iam')
    
    try:
        access_keys = client.list_access_keys(
            UserName = username
        ).get('AccessKeyMetadata', [])
    except Exception as ex:
        return jsonify(error="user not found"), 404

    details = []

    for key in access_keys:
        
        key_info = client.get_access_key_last_used(
            AccessKeyId = key['AccessKeyId']
        ).get('AccessKeyLastUsed', {})

        if len(key_info) != 0:
            det = {
                'AccessKeyId': key['AccessKeyId'],
                'Status': key['Status'],
                'LastUsedDate': str(key_info['LastUsedDate'])\
                     if key['Status'] == 'Active' else None,
                'CreatedTime': str(key['CreateDate'])
            }
            details.append(det)
    
    return {'accessKeyDetails': details}

@app.route('/get-object/', methods = ['GET'])
def get_s3_obj():
    s3 = boto3.client('s3')

    with open('/tmp/s3_obj', 'wb') as data:
        s3.download_fileobj('gautham-assignment-1', 'nginx.conf', data)

    return send_file('/tmp/s3_obj')

if __name__ == "__main__":
    app.run()