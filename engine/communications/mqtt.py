import paho.mqtt.client as mqtt_client


class Broker:
    # The callback for when the client receives a CONNACK response from the server.
    def __init__(self, topic):
        self.topic = topic
        self.devices = {}

    def on_connect(self, client, userdata, flags, reason_code, properties):
        print(f"Connected with result code {reason_code}")
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe(self.topic + "/#")

    def add_device(self, device):
        self.devices[device.name] = device


    def on_message(self, client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))
        device_name = msg.topic.split("/")[1] 
        if device_name in self.devices:
            self.devices[device_name].state = msg.payload


    def start(self):
        self.client = mqtt_client.Client(
            mqtt_client.CallbackAPIVersion.VERSION2
        )
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        print("Topic: " + self.topic + "/#")
        # client.subscribe("#")
        self.client.username_pw_set("openhabian", "ohPinno9!")
        self.client.connect("192.168.2.130", 1883, 60)
        self.client.loop_start()

    def set_state(self, device, property, state):
        print(
            self.topic
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
        print(
            self.topic
            + "/"
            + device
            + "/get"
            + '{ "'
            + property
            + '": ""}'
        )
        self.client.publish(self.topic + "/" + device + "/get", 
                            '{ "' + property + '": ""}',)

    def stop(self):
        self.client.loop_stop()
        self.client.disconnect()
