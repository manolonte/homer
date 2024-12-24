from devices.device import Device

class Sensor(Device):
    def __init__(self, name, zone, engine):
        super().__init__(name, zone, engine)
        self.probe_property = "linkquality"
