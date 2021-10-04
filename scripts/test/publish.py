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

print("publishing data to all sensors")

send_msg1 = {
    'temperature':"" ,
    'humidity': round(random.randint(20, 80))
}
client.publish(config['mqtt']['sensor_topic']+"/1", payload=json.dumps(send_msg1))
print(config['mqtt']['sensor_topic'])
send_msg2 = {
    'temperature': random.uniform(16.0, 22.0),
    'humidity': round(random.randint(20, 80))
}
client.publish(config['mqtt']['sensor_topic']+"/2", payload=json.dumps(send_msg2))

send_msg3 = {
    'temperature': random.uniform(16.0, 22.0),
    'humidity': round(random.randint(20, 80))
}
client.publish(config['mqtt']['sensor_topic']+"/3", payload=json.dumps(send_msg3))

send_msg4 = {
    'temperature': random.uniform(16.0, 35.0),
    'humidity': round(random.randint(20, 80))
}
client.publish(config['mqtt']['sensor_topic']+"/4", payload=json.dumps(send_msg4))
