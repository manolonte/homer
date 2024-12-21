import time

from devices import Plug, Switch, Sensor
from engine import Engine


def main():
    engine = Engine("config.json")
    
    engine.start()
    time.sleep(5)

    print("Enchufe sofa: " + engine.devices["enchufe_sofa"].get_state())
    print("Enchufe tele: " + engine.devices["enchufe_tele"].get_state())

    engine.devices["enchufe_sofa"].set_property("state", "ON")

    print("Enchufe sofa: " + engine.devices["enchufe_sofa"].get_state())

    engine.devices["enchufe_sofa"].set_property("state", "OFF")

    print("Enchufe sofa: " + engine.devices["enchufe_sofa"].get_state())

    engine.configure_device("interruptor_salon", "Switch", "salon")

    while True:
        pass

    engine.stop()


if __name__ == "__main__":
    main()
