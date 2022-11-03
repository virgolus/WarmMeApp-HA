#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import paho.mqtt.client as mqtt
import random
import json
import configparser
import logging


# Read properties
config = configparser.ConfigParser()
config.read('/home/pi/warmme.properties')
logging.basicConfig(filename='/home/pi/WarmMeApp-HA/logs/warmme-adapter.log', filemode='w',format='%(asctime)s - %(message)s', level=logging.DEBUG)

broker=config['mqtt']['url']
# create mqtt connection
client= mqtt.Client()

def on_publish(client,userdata,result):
    print('mandato')

print("connecting to broker ",broker)
client.on_publish=on_publish
client.connect(broker) #connect

command_topic=config['mqtt']['actuator_topic']+"/4/command"
state_topic=config['mqtt']['actuator_topic']+"/4/state"
print(state_topic)

#logging.debug("topic: "+state_topic+" payload: "+str('OFF'))
logging.debug("topic: "+command_topic+" payload: "+str('OFF'))
client.publish(command_topic,payload='OFF')
#client.publish(state_topic,payload='OFF')



# print("publishing data to all sensors")

# send_msg1 = {
#     'temperature': random.uniform(16.0, 22.0),
#     'humidity': round(random.randint(20, 80))
# }
# client.publish(config['mqtt']['sensor_topic']+"/1", payload=json.dumps(send_msg1))
# print(config['mqtt']['sensor_topic'])
# send_msg2 = {
#     'temperature': random.uniform(16.0, 22.0),
#     'humidity': round(random.randint(20, 80))
# }
# client.publish(config['mqtt']['sensor_topic']+"/2", payload=json.dumps(send_msg2))

# send_msg3 = {
#     'temperature': random.uniform(16.0, 22.0),
#     'humidity': round(random.randint(20, 80))
# }
# client.publish(config['mqtt']['sensor_topic']+"/3", payload=json.dumps(send_msg3))

# send_msg4 = {
#     'temperature': random.uniform(16.0, 35.0),
#     'humidity': round(random.randint(20, 80))
# }
# client.publish(config['mqtt']['sensor_topic']+"/4", payload=json.dumps(send_msg4))
