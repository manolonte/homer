class Device:
    def __init__(self, name, zone, broker):
        self.name = name
        self.zone = zone
        self.broker = broker
        self.state = ""
        broker.add_device(self)
