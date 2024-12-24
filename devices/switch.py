from devices.switchable_device import SwitchableDevice


class Switch(SwitchableDevice):
    def __init__(self, name, zone, engine):
        super().__init__(name, zone, engine)
