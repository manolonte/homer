import importlib
import inspect
import os
import engine.communications.mqtt as mqtt

class Engine:
    def __init__(self, config):
        self.config = config
        self.devices = {}
        self.rules = self.load_rules()
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

    def start(self):
        self.broker.start()
        for rule in self.rules:
            rule.execute()
    
    def stop(self):
        self.broker.stop()
