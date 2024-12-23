import time
from .rule import Rule

class SensorCalentadorRule(Rule):
    def execute(self):
        print("SensorCalentadorRule")
        self.engine.devices["interruptor_agua_caliente"].off()
    
    def when_sensor(self):
        condition = {"device": "sensor_salon", 
                     "property": "occupancy", 
                     "value": True}

        action = self.execute

        return condition, action

    def when_enchufe(self):
        condition = {"device": "enchufe_esquina_salon", 
                     "property": "state", 
                     "value": "ON"}

        action = self.execute

        return condition, action
