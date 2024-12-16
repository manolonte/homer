from devices.device import Device


class Alarm(Device):
    def __init__(self, name, zone, broker):
        super().__init__(name, zone, broker)
