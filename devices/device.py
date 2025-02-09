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
        self.state = state.decode("utf-8")
        self.properties = json.loads(state)

    def get_state(self):
        return self.state

    def get_data(self):
        return self.name, self.zone, self.state, self.properties
    
    def set_property(self, property, value):
        self.engine.broker.set_state(self.name, property, value)
        self.properties[property] = value
        self.state = json.dumps(self.properties)
    
    def set(self, property, value):
        self.set_property(property, value)

    def get_property(self, property):
        return self.properties[property]
    
    def get(self, property):
        return self.get_property(property)
