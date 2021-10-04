#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import paho.mqtt.client as mqtt
import random
import json
import configparser

# Read properties
config = configparser.ConfigParser()
config.read('/home/pi/warmme.properties')

broker=config['mqtt']['url']

# create mqtt connection
client= mqtt.Client()

print("connecting to broker ",broker)
client.connect(broker) #connect

print("publishing data to sensor 1")

send_msg1 = {
    'temperature': random.uniform(16.0, 22.0),
    'humidity': round(random.randint(20, 80)),
    'battery': 3.00
}
client.publish(config['mqtt']['sensor_topic']+"/1", payload=json.dumps(send_msg1))
print(config['mqtt']['sensor_topic'])
