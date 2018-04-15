#!flask/bin/python
import json
from flask import Flask, Response
from helloworld.flaskrun import flaskrun

import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0])))

application = Flask(__name__)

@application.route('/', methods=['GET'])
def get():
    return Response(json.dumps({'Output': 'Hello World'}), mimetype='application/json', status=200)

@application.route('/get_ip', methods=['GET'])
def get_ip():
    return Response(json.dumps(get_ip_meta()), mimetype='application/json', status=200)

@application.route('/', methods=['POST'])
def post():
    return Response(json.dumps({'Output': 'Hello World'}), mimetype='application/json', status=200)

import requests
import json
def get_ip_meta():
    user_ip = str(requests.environ['REMOTE_ADDR'])
    service_url = 'http://ipinfo.io/{}'.format(user_ip) 
    return requests.get(service_url).json()

if __name__ == '__main__':
    flaskrun(application)
