import json

class Device:
    def __init__(self, name, zone, broker):
        self.name = name
        self.zone = zone
        self.broker = broker
        self.state = ""
        broker.add_device(self)
        self.probe_property = "linkquality"
        self.properties = {}

    def set_state(self,state):
        self.state = state
        self.properties = json.loads(state)

    def get_state(self):
        return self.state

    def get_data(self):
        return self.name, self.zone, self.state, self.properties
    
    def set_property(self, property, value):
        self.broker.set_state(self.name, property, value)
        self.properties[property] = value
