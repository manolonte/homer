from components.onoff import OnOff
from devices.device import Device


class Plug(Device):
    def __init__(self, name, zone, broker):
        super().__init__(name, zone, broker)
        self.onoff = OnOff("onoff", self)

    def on(self):
        self.onoff.on()

    def off(self):
        self.onoff.off()
