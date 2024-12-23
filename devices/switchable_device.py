from devices.device import Device


class SwitchableDevice(Device):
    def __init__(self, name, zone, engine):
        super().__init__(name, zone, engine)
        self.probe_property = "state"
        # self.onoff = OnOff("onoff", self)

    def on(self):
        self.set_property("state", "ON")

    def off(self):
        self.set_property("state", "OFF")
    