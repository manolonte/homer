import communications.mqtt as mqtt
import time


def main():
    broker = mqtt.Broker('zigbee2mqtt')
    broker.start()

    broker.set_state('interruptor_cocina', 'state', 'ON')
    time.sleep(5)
    broker.set_state('interruptor_cocina', 'state', 'OFF')
    broker.set_state('enchufe_esquina_salon', 'state', 'ON')
    time.sleep(5)
    broker.set_state('enchufe_esquina_salon', 'state', 'OFF')

    broker.stop()

if  __name__ == "__main__":
    main()
