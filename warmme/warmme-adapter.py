#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import paho.mqtt.client as mqtt
import pathlib
import os
import configparser
import logging
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PumpsMapping={
    '1':16, #sala
    '2':20, #notte
    '3':21  #bagno
    '4':19  #laboratorio
}
for GpioOut in PumpsMapping.values():
    GPIO.setup(GpioOut,GPIO.OUT)

# Read properties
config = configparser.ConfigParser()
config.read('/home/pi/warmme.properties')

logging.basicConfig(filename='/home/pi/WarmMeApp-HA/logs/warmme-adapter.log', filemode='w',format='%(asctime)s - %(message)s', level=logging.DEBUG)

# mqtt client
broker=config['mqtt']['url']

def sendstate(msg):
    clean_payload = str(msg.payload).split("'")[1]
    path=pathlib.PurePath(str(msg.topic))
    state_topic=os.path.join(path.parents[0],'state')
    logging.debug("state topic: "+state_topic+" payload: "+str(clean_payload))
    mqttc.publish(state_topic,clean_payload)

def setRelays(msg):
    clean_payload = str(msg.payload).split("'")[1]
    path=pathlib.PurePath(str(msg.topic))
    PumpNumber=path.parents[0].name
    GpioNumber=PumpsMapping[PumpNumber]
    if clean_payload=='ON':
        GPIO.output(GpioNumber,GPIO.HIGH)
    else:
        GPIO.output(GpioNumber,GPIO.LOW)    
    return True

def on_connect(mqttc, obj, flags, rc):
    logging.debug("connected to mqtt")

def on_message(mqttc, obj, msg):
    # if relais activation is ok, set state according to src message body
    logging.debug("topic: " + msg.topic + " payload: " + str(msg.payload))
    if (setRelays(msg)):sendstate(msg)

def on_subscribe(mqttc, obj, mid, granted_qos):
    logging.debug("Subscribed: " + str(mid) + " qos: " + str(granted_qos))

#�connect to mqtt
mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.connect(broker)
mqttc.subscribe(config['mqtt']['command_all_topic'], 0)

mqttc.loop_forever()