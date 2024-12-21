from devices.switchable_device import SwitchableDevice


class Plug(SwitchableDevice):
    def __init__(self, name, zone, broker):
        super().__init__(name, zone, broker)
