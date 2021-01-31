#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import paho.mqtt.client as mqtt
import pathlib
import os
import configparser
import logging

# Read properties
config = configparser.ConfigParser()
config.read('/home/pi/warmme.properties')

logging.basicConfig(filename='/home/pi/WarmMeApp-HA/logs/subscribe.log', filemode='w',format='%(asctime)s - %(message)s', level=logging.DEBUG)

# mqtt client
broker=config['mqtt']['url']

def on_connect(mqttc, obj, flags, rc):
    print("connected to mqtt")
    logging.debug("connected to mqtt")

def on_message(mqttc, obj, msg):
    print("topic: " + msg.topic + " qos: " + str(msg.qos) + " payload: " + str(msg.payload))
    logging.debug("topic: " + msg.topic + " payload: " + str(msg.payload))
    # set state according to src message body
    # clean_payload = str(msg.payload).split("'")[1]
    # path = pathlib.PurePath(str(msg.topic))
    # state_topic = os.path.join(*path.parts[:-1]) + '/state'
    #print(state_topic)
    # mqttc.publish(state_topic, clean_payload)

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed. topic: "+config['mqtt']['sensor_topic'])
    logging.debug("Subscribed: " + str(mid) + " qos: " + str(granted_qos))

#�connect to mqtt
mqttc = mqtt.Client()
mqttc.on_connect=on_connect
mqttc.on_message = on_message
mqttc.on_subscribe=on_subscribe
mqttc.connect(broker)
# mqttc.subscribe(config['mqtt']['command_all_topic'], 0)
mqttc.subscribe(config['mqtt']['sensor_topic']+"/#", 0)
# mqttc.subscribe(config['mqtt']['sensor_topic'], 0)
mqttc.loop_forever()
