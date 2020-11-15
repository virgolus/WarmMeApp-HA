import time
import paho.mqtt.client as mqtt
import random
import json

broker="192.168.1.49"

client= mqtt.Client() #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")

# Set default thermostat state
print("set all pumps off")
client.publish("home-assistant/pump/1/state", "ON")
client.publish("home-assistant/pump/2/state", "ON")
client.publish("home-assistant/pump/3/state", "ON")
client.publish("home-assistant/pump/4/state", "ON")
# round(random.uniform(16.0, 35.0)))
