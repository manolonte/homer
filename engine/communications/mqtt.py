import paho.mqtt.client as mqtt_client

class Broker:
# The callback for when the client receives a CONNACK response from the server.
    def __init__(self, topic):
        self.topic = topic

    def on_connect(self, client, userdata, flags, reason_code, properties):
        print(f"Connected with result code {reason_code}")
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        #client.subscribe("$SYS/#")
        #client.subscribe(self.topic)
        client.subscribe(self.topic)


    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))

    def start(self):
        self.client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION2)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        print("Topic: " + self.topic + "/#")
        #client.subscribe("#")
        self.client.username_pw_set("openhabian", "ohPinno9!")
        self.client.connect("192.168.2.130", 1883, 60)
        self.client.loop_start()

    def set_state(self, device, property, state):
        print(self.topic + "/" + device + "/set" + "{ \"" + property + "\": \"" + state + "\"}")
        self.client.publish(self.topic + "/" + device + "/set", "{ \"" + property + "\": \"" + state + "\"}")

    def stop(self):
        self.client.loop_stop()
        self.client.disconnect()
