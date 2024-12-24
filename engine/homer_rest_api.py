# REST API interface for Homer
import json
from flask import Flask, request, jsonify

app = Flask(__name__)
class RestApi:
    def __init__(self, engine, host, port):
        self.engine = engine
        self.app = app
        self.host = host
        self.port = port

    def run(self):
        #self.app.add_url_rule('/devices', 'devices', self.engine.devices)
        self.app.add_url_rule('/get_config', 'get_config', self.get_config, methods=['GET'])
        self.app.add_url_rule('/get_device/<device_name>', 'getconfig', self.get_device, methods=['GET'])
        self.app.add_url_rule('/get_devices', 'get_devices', self.get_devices, methods=['GET'])
        self.app.add_url_rule('/get_config', 'get_config', self.get_config, methods=['GET'])        
        self.app.add_url_rule('/set_device_property/<device_name>', 'set_device_property', self.set_device_property, methods=['GET','POST'])
        self.app.run(host = self.host, port = self.port)

    def get_config(self):
        return self.engine.config_json
    
    def get_device(self, device_name):
        return self.engine.devices[device_name].state
    
    def get_devices(self):
        devices_json = []
        for device in self.engine.devices:
            device_json = {
                "device": device,
                "state": self.engine.devices[device].properties,
            }
            devices_json.append(device_json)
        return json.dumps(devices_json)

    def get_config(self):
        return self.engine.config_json
    
    def set_device_property(self, device_name):
        content = request.json
        self.engine.devices[device_name].set_property(content["property"], content["value"])
        return self.engine.devices[device_name].state
