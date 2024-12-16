from components.component import Component


class OnOff(Component):
    def __init__(self, name, device):
        super().__init__(name, device)

    def set_state(self, state):
        self.device.broker.set_state(self.device.name, "state", state)

    def on(self):
        self.set_state("ON")

    def off(self):
        self.set_state("OFF")
