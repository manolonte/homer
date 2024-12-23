import json
from devices.device import Device

class Virtual(Device):
    def __init__(self, name, zone, engine):
        super().__init__(name, zone, engine)

    def set_property(self, property, value):
        self.engine.logger.info("Virtual " + self.name +  " - Setting property: " + property + " to " + value)
        self.properties[property] = value
        self.state = json.dumps(self.properties)
        self.engine.evaluate_when(self)
