from devices.device import Device


class SwitchableDevice(Device):
    def __init__(self, name, zone, broker):
        super().__init__(name, zone, broker)
        self.probe_property = "state"
        # self.onoff = OnOff("onoff", self)

    def on(self):
        self.set_property("state", "ON")

    def off(self):
        self.set_property("state", "OFF")
    