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

logging.basicConfig(filename='/home/pi/WarmMeApp-HA/logs/warmme-adapter.log', filemode='w',format='%(asctime)s - %(message)s', level=logging.DEBUG)

# mqtt client
broker=config['mqtt']['url']

def on_connect(mqttc, obj, flags, rc):
    logging.debug("connected to mqtt")

def on_message(mqttc, obj, msg):
    #print("topic: " + msg.topic + " qos: " + str(msg.qos) + " payload: " + str(msg.payload))
    logging.debug("topic: " + msg.topic + " payload: " + str(msg.payload))
    # set state according to src message body
    clean_payload = str(msg.payload).split("'")[1]
    path = pathlib.PurePath(str(msg.topic))
    state_topic = os.path.join(*path.parts[:-1]) + '/state'
    #print(state_topic)
    mqttc.publish(state_topic, clean_payload)

def on_subscribe(mqttc, obj, mid, granted_qos):
    logging.debug("Subscribed: " + str(mid) + " qos: " + str(granted_qos))

#Âconnect to mqtt
mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.connect(broker)
mqttc.subscribe(config['mqtt']['command_all_topic'], 0)

