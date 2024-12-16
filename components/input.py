from components.component import Component


class Input(Component):
    def __init__(self, name, device, units, type):
        super().__init__(name, device)
        self.units = units
        self.type = type
        self.state = ""
    
    def read(self):
        return self.device.broker.get_state(self.device.name, 'state')
