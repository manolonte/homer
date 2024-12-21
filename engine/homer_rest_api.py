# REST API interface for Homer
import json
from flask import Flask, request

app = Flask(__name__)
class RestApi:
    def __init__(self, engine):
        self.engine = engine
        self.app = app

    def run(self):
        #self.app.add_url_rule('/devices', 'devices', self.engine.devices)
        self.app.run(host='0.0.0.0', port=5000)
