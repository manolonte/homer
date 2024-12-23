import time
from .rule import Rule

class SensorSalonAlarma(Rule):
    def alarma(self):
        print("STATE " + self.engine.devices["sensor_salon"].state)
        print("OCCUPANCY: " + str(self.engine.devices["sensor_salon"].get("occupancy")))
        if self.engine.devices["sensor_salon"].get("occupancy") == False:
            print("ALARMA!!!")
            
    
    def when_no_estamos_en_casa(self):
        condition = {"device": "estamos_en_casa", 
                     "property": "value", 
                     "value": "False"}

        action = self.alarma

        return condition, action
