from components.input import Input
from devices.device import Device


class Sensor(Device):
    def __init__(self, name, zone, broker):
        super().__init__(name, zone, broker)
        self.occupancy = Input("occupancy", self, "", "occupancy")

    def read(self):
        self.occupancy.read()
