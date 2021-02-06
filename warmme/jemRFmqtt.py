
#!/usr/bin/env python
import sys
from threading import Thread
#from bme280 import process_bme_reading
from rflib import rf2serial, fetch_messages, request_reply
import rflib
from time import sleep
import time
import configparser
import paho.mqtt.client as mqtt
import json
import logging
from random import randint

config = configparser.ConfigParser()
config.read('/home/pi/warmme.properties')
logging.basicConfig(filename='/home/pi/WarmMeApp-HA/logs/Sensors.log', filemode='w',format='%(asctime)s - %(message)s', level=logging.DEBUG)
broker=config['mqtt']['url']

class sensor:
    def __init__(self,id,HAid):
        self.id=id
        self.HAid=HAid
        self.temp=""
        self.hum=""
        self.battery=""
    def Updatevalue(self,value):
	msgReady=False
	if "BATT" in value:
	    self.battery=value[4:-1]
        if "TMPA" in value and not '-' in value:
            self.temp=value[4:]
        if "HUM" in value:
            self.hum=value[3:]
            msgReady=True
        return msgReady

ListofSensors={
    '94':sensor('94','1'),
    '95':sensor('95','2'),
    '96':sensor('96','3'),
    '93':sensor('93','4')
}

def on_publish(client,userdata,result):
    logging.debug("data published")

def inbound_message_processing():
  try:
    while (True):
        sleep(0.2)
        fetch_messages(0);
        while len(rflib.processing_queue)>0:
            message = rflib.processing_queue.pop(0)
            logging.debug("sensorID: " + message[0] + " message: " +message[1])
            ######QUI FARE COSE
            if message[0] in ListofSensors:
              Mysensor=ListofSensors[message[0]]
              if Mysensor.Updatevalue(message[1])==True:
                jsonMessage={
                  'temperature':Mysensor.temp,
                  'humidity':Mysensor.hum,
		  'battery':Mysensor.battery
                }
                topic=config['mqtt']['sensor_topic']+"/"+Mysensor.HAid
                client= mqtt.Client("pi_rf_"+str(randint(0, 100)))
                client.on_publish=on_publish
                client.connect(broker) #connect
                client.publish(topic,payload=json.dumps(jsonMessage))
                logging.debug(topic)
                logging.debug(json.dumps(jsonMessage))

        if rflib.event.is_set():
            break
  except Exception as e: 
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(e).__name__, e.args)
        logging.error(e)
        rflib.event.set()
        exit()

def main(): 
  # client= mqtt.Client("pi_rf_"+str(randint(0, 100)))
  # client.on_publish=on_publish
  # client.connect(broker) #connect

  rflib.init()

  #start serial processing thread
  a=Thread(target=rf2serial, args=())
  a.start()

  #now start processing thread
  b=Thread(target=inbound_message_processing, args=())
  b.start()

  while not rflib.event.is_set():
      try:
          sleep(1)
      except KeyboardInterrupt:
          rflib.event.set()
          break
  print rflib.event.is_set()

if __name__ == "__main__":
    try:
      main()
    except Exception as e:
      template = "An exception of type {0} occurred. Arguments:\n{1!r}"
      message = template.format(type(e).__name__, e.args)
      print message
      print e
      rflib.event.set()
    finally:
      rflib.event.set()
      exit()
