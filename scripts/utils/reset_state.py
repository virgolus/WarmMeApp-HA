#!/usr/bin/python3

import time
import paho.mqtt.client as mqtt
import random
import json
import configparser

# Read properties
config = configparser.ConfigParser()
config.read('/home/pi/warmme.properties')

broker=config['mqtt']['url']

client= mqtt.Client() #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")

print("connecting to broker ",broker)
client.connect(broker) #connect

print("Reset pumps and thermostat state")

client.publish(config['mqtt']['actuator_topic']+"/1/state", payload="OFF")
client.publish(config['mqtt']['actuator_topic']+"/1/command", payload="OFF")
client.publish(config['mqtt']['actuator_topic']+"/2/state", payload="OFF")
client.publish(config['mqtt']['actuator_topic']+"/2/command", payload="OFF")
client.publish(config['mqtt']['actuator_topic']+"/3/state", payload="OFF")
client.publish(config['mqtt']['actuator_topic']+"/3/command", payload="OFF")
client.publish(config['mqtt']['actuator_topic']+"/4/state", payload="OFF")
client.publish(config['mqtt']['actuator_topic']+"/4/command", payload="OFF")
