import time

import engine.communications.mqtt as mqtt
from devices import Plug, Switch, Sensor


def main():
    broker = mqtt.Broker("zigbee2mqtt")

    enchufe = Plug("enchufe_esquina_salon", "salon", broker)
    luz = Switch("interruptor_cocina", "cocina", broker)
    sensor_salon = Sensor("sensor_salon", "salon", broker)
    interruptor_agua_caliente= Plug("interruptor_agua_caliente", "buhardilla", broker)
    
    broker.start()
    
    interruptor_agua_caliente.off()
    time.sleep(5)
    #interruptor_agua_caliente.off()
    
    # # luz.on()
    # # time.sleep(5)
    # # luz.off()

    #time.sleep(20)

    print(sensor_salon.get_data())
    print(enchufe.get_data())
    print(luz.get_data())
    print(interruptor_agua_caliente.get_data())    
    print(interruptor_agua_caliente.properties["countdown"])

    broker.stop()


if __name__ == "__main__":
    main()
