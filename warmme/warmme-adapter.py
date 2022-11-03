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

# HomeAssistant pumps topic - GPIO mapping
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PumpsMapping = {
    '1': 16, #sala
    '2': 20, #notte
    '3': 21, #bagno
    '4': 19, #laboratorio
    '5': 26  #caldaia
}

for GpioOut in PumpsMapping.values():
    GPIO.setup(GpioOut,GPIO.OUT)
    GPIO.output(GpioOut,GPIO.HIGH)

# Read properties
config = configparser.ConfigParser()
config.read('/home/pi/warmme.properties')

logging.basicConfig(filename='/home/pi/WarmMeApp-HA/logs/warmme-adapter.log',
    filemode='a',
    level=logging.DEBUG,
    format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
    datefmt='%Y-%m-%dT%H:%M:%S')

# mqtt client
broker=config['mqtt']['url']

def sendstate(msg):
    clean_payload = str(msg.payload).split("'")[1]
    path = pathlib.PurePath(str(msg.topic))
    state_topic = os.path.join(path.parents[0], 'state')
    logging.debug("update state -> topic: " + state_topic + " payload: " + str(clean_payload))
    mqttc.publish(state_topic, clean_payload)

def setRelays(msg):
    clean_payload = str(msg.payload).split("'")[1]
    path=pathlib.PurePath(str(msg.topic))
    PumpNumber=path.parents[0].name
    GpioNumber=PumpsMapping[PumpNumber]
    if clean_payload == 'ON':
        logging.debug('OOOOOOOON')
        GPIO.output(GpioNumber,GPIO.LOW)
    else:
        logging.debug('OFFFFFFFFF')
        GPIO.output(GpioNumber,GPIO.HIGH)
    logging.debug('set relais state -> GPIO ' + str(GpioNumber) + ' set: ' + str(GPIO.input(GpioNumber)))

def on_connect(mqttc, obj, flags, rc):
    logging.debug("connected to mqtt" + config['mqtt']['url'])

def on_message(mqttc, obj, msg):
    # if relais activation is ok, set state according to src message body
    logging.debug("msg received -> topic: " + msg.topic + " payload: " + str(msg.payload))
    setRelays(msg)
    sendstate(msg)

def on_subscribe(mqttc, obj, mid, granted_qos):
    logging.debug("subscribed to " + config['mqtt']['command_all_topic'])

#�connect to mqtt
mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_subscribe= on_subscribe
mqttc.on_connect=on_connect
mqttc.connect(broker)
mqttc.subscribe(config['mqtt']['command_all_topic'], 0)

mqttc.loop_forever()
