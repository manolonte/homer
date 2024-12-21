# REST API interface for Homer
import json
from flask import Flask, request, jsonify

app = Flask(__name__)
class RestApi:
    def __init__(self, engine):
        self.engine = engine
        self.app = app

    def run(self):
        #self.app.add_url_rule('/devices', 'devices', self.engine.devices)
        self.app.add_url_rule('/get_config', 'get_config', self.get_config, methods=['GET'])
        self.app.add_url_rule('/get_device_state/<device_name>', 'getconfig', self.get_device_state, methods=['GET'])
        self.app.add_url_rule('/set_device_property/<device_name>', 'set_device_property', self.set_device_property, methods=['GET','POST'])
        self.app.run(host='0.0.0.0', port=5000)

    def get_config(self):
        return self.engine.config_json
    
    def get_device_state(self, device_name):
        return self.engine.devices[device_name].state
    
    def set_device_property(self, device_name):
        content = request.json
        self.engine.devices[device_name].set_property(content["property"], content["value"])
        return self.engine.devices[device_name].state
