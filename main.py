import time

import engine.communications.mqtt as mqtt
from devices import Plug, Switch, Sensor


def main():
    broker = mqtt.Broker("zigbee2mqtt")

    enchufe = Plug("enchufe_esquina_salon", "salon", broker)
    luz = Switch("interruptor_cocina", "cocina", broker)
    sensor_salon = Sensor("sensor_salon", "salon", broker)
    
    broker.start()
    
    enchufe.on()
    time.sleep(5)
    enchufe.off()
    
    # # luz.on()
    # # time.sleep(5)
    # # luz.off()

    time.sleep(20)

    print(sensor_salon.get_data())
    print(enchufe.get_data())
    print(luz.get_data())

    broker.stop()


if __name__ == "__main__":
    main()
