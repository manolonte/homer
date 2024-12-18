import time
from .rule import Rule

class SensorCalentadorRule(Rule):
    def execute(self):
        print("SensorCalentadorRule")
        self.engine.devices["interruptor_agua_caliente"].off()
    
    def when(self):
        condition = {"device": "sensor_salon", 
                     "property": "occupancy", 
                     "value": True}

        action = self.execute()

        return condition, action
