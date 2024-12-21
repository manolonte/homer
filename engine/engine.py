import importlib
import inspect
import os
import time
import engine.communications.mqtt as mqtt
import json
from devices import *

class Engine:
    def __init__(self, config):
        self.config = config
        self.devices = {}
        self.read_configuration()
        self.rules = self.load_rules()
        self.when = self.load_when()
        self.broker = mqtt.Broker("zigbee2mqtt",self)


    def add_device(self, device):
        self.devices[device.name] = device

    def add_broker(self, broker):
        self.broker = broker

    # imports all rules classes in rules directory and instantiates them
    def load_rules(self):
        rules = []
        for rule in os.listdir("rules"):
            if rule.endswith(".py") and rule != "__init__.py":
                rule = rule[:-3]
                module = importlib.import_module(f"rules.{rule}")
                for name, obj in inspect.getmembers(module):
                    if inspect.isclass(obj):
                        rules.append(obj(self))
        return rules

    def load_when(self):
        when = []
        for rule in self.rules:
            # Execute all when methods in rules (methods that start with when_)
            for method in inspect.getmembers(rule, predicate=inspect.ismethod):
                if method[0].startswith("when"):
                    condition_and_action = getattr(rule, method[0])()
                    when.append({ "condition": condition_and_action[0], "action": condition_and_action[1]})
        return when

    def start(self):
        self.broker.start()
        time.sleep(10)
        self.broker.evaluate_when = True
    
    def stop(self):
        self.broker.stop()

    def evaluate_when(self, device):
        print("Evaluating when for " + device.name)
        for when in self.when:
            if when["condition"] == None:
                print("No condition")
                continue
            if when["condition"]["device"] == device.name:
                if device.properties[when["condition"]["property"]] == when["condition"]["value"]:
                    print("Condition met")
                    when["action"]()

    def read_configuration(self):
        with open(self.config) as f:
            self.config_json = json.load(f)
        for device in self.config_json["devices"]:
            # Dynamically load device classes based on config file
            device_class = globals()[device["type"].capitalize()]
            self.devices["name"] = device_class(device["name"], device["zone"], self)

    def configure_device(self, name, type, zone):
        device = globals()[type.capitalize()](name, zone, self)
        self.devices[name] = device
        self.config_json["devices"].append({"name": device.name, "type": device.__class__.__name__, "zone": device.zone})
        # Format json and write to file
        with open(self.config, "w") as f:
            json.dump(self.config_json, f, indent=4)
            