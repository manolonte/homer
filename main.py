import time

from devices import Plug, Switch, Sensor
from engine import Engine


def main():
    engine = Engine("config.json")
    

    enchufe = Plug("enchufe_esquina_salon", "salon", engine)
    luz = Switch("interruptor_cocina", "cocina", engine)
    sensor_salon = Sensor("sensor_salon", "salon", engine)
    interruptor_agua_caliente= Plug("interruptor_agua_caliente", "buhardilla", engine)
    
    engine.start()
    time.sleep(5)

    print(interruptor_agua_caliente.properties["countdown"])

    engine.stop()


if __name__ == "__main__":
    main()
