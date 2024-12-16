from components.onoff import OnOff
from devices.switchable_device import SwitchableDevice


class Switch(SwitchableDevice):
    def __init__(self, name, zone, broker):
        super().__init__(name, zone, broker)
        self.onoff = OnOff("onoff", self)
