import time
import paho.mqtt.client as mqtt
import pathlib
import os

broker="192.168.1.49"

def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))


def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    clean_payload = str(msg.payload).split("'")[1]
    path = pathlib.PurePath(str(msg.topic))
    state_topic = os.path.join(*path.parts[:-1]) + '/state'
    print(state_topic)
    mqttc.publish(state_topic, clean_payload)

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print(string)


# If you want to use a specific client id, use
# mqttc = mqtt.Client("client-id")
# but note that the client id must be unique on the broker. Leaving the client
# id parameter empty will generate a random id for you.
mqttc = mqtt.Client()
mqttc.on_message = on_message
#mqttc.on_connect = on_connect
#mqttc.on_subscribe = on_subscribe
# Uncomment to enable debug messages
# mqttc.on_log = on_log
mqttc.connect(broker)
mqttc.subscribe("home-assistant/pump/+/command", 0)

mqttc.loop_forever()
