import json

class Device:
    def __init__(self, name, zone, engine):
        self.name = name
        self.zone = zone
        self.engine = engine
        self.state = ""
        engine.add_device(self)
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
        self.engine.broker.set_state(self.name, property, value)
        self.properties[property] = value
