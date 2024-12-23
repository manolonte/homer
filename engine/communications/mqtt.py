import paho.mqtt.client as mqtt_client
import time


class Broker:
    # The callback for when the client receives a CONNACK response from the server.
    def __init__(self, topic, engine, host, port, username, password):
        self.topic = topic
        self.client = None
        self.engine = engine
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.evaluate_when = False
        engine.add_broker(self)

    def on_connect(self, client, userdata, flags, reason_code, properties):
        self.engine.logger.info("Connected with result code " + str(reason_code))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe(self.topic + "/#")


    def on_message(self, client, userdata, msg):
        self.engine.logger.info(msg.topic + " " + str(msg.payload))
        device_name = msg.topic.split("/")[1] 
        if device_name in self.engine.devices:
            self.engine.devices[device_name].set_state(msg.payload)
            if self.evaluate_when:
                self.engine.evaluate_when(self.engine.devices[device_name])


    def start(self):
        self.client = mqtt_client.Client(
            mqtt_client.CallbackAPIVersion.VERSION2
        )
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.engine.logger.info("Topic: " + self.topic + "/#")
        self.client.username_pw_set(self.username, self.password)
        self.client.connect(self.host, self.port, 60)
        self.client.loop_start()
        time.sleep(5)
        for device_name in self.engine.devices:
              if self.engine.devices[device_name].probe_property != "" and not self.engine.devices[device_name].state :
                self.client.publish(self.topic + "/" + device_name + "/get", '{"' + self.engine.devices[device_name].probe_property + '": ""}')


    def set_state(self, device, property, state):
        self.engine.logger.info(self.topic
            + "/"
            + device
            + "/set"
            + '{ "'
            + property
            + '": "'
            + state
            + '"}'
        )
        self.client.publish(
            self.topic + "/" + device + "/set",
            '{ "' + property + '": "' + state + '"}',
        )


    def get_state(self, device, property):
        self.client.publish(self.topic + "/" + device + "/get", 
                            '{ "' + property + '": ""}',)

    def stop(self):
        self.client.loop_stop()
        self.client.disconnect()
