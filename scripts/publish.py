import time
import paho.mqtt.client as mqtt
import random
import json

broker="192.168.1.49"

client= mqtt.Client() #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")

print("connecting to broker ",broker)
client.connect(broker) #connect

print("publishing data to all sensors")

send_msg1 = {
    'temperature': random.uniform(16.0, 35.0),
    'humidity': round(random.randint(20, 80))
}
client.publish("home-assistant/th/1", payload=json.dumps(send_msg1))

send_msg2 = {
    'temperature': random.uniform(16.0, 35.0),
    'humidity': round(random.randint(20, 80))
}
client.publish("home-assistant/th/2", payload=json.dumps(send_msg2))

send_msg3 = {
    'temperature': random.uniform(16.0, 35.0),
    'humidity': round(random.randint(20, 80))
}
client.publish("home-assistant/th/3", payload=json.dumps(send_msg3))

send_msg4 = {
    'temperature': random.uniform(16.0, 35.0),
    'humidity': round(random.randint(20, 80))
}
client.publish("home-assistant/th/4", payload=json.dumps(send_msg4))
