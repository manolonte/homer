from components.input import Input
from devices.device import Device


class Sensor(Device):
    def __init__(self, name, zone, broker):
        super().__init__(name, zone, broker)
        self.probe_property = "linkquality"
