class Device:
    def __init__(self, name, zone, broker):
        self.name = name
        self.zone = zone
        self.broker = broker
        self.state = ""
        broker.add_device(self)

    def set_state(self,state):
        self.state = state

    def get_state(self):
        return self.state

    def get_data(self):
        return self.name, self.zone, self.state
