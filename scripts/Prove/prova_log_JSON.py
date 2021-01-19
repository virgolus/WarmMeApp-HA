# -*- coding: utf-8 -*-
import time
import paho.mqtt.client as mqtt
import pathlib
import os
import configparser
import logging

logging.basicConfig(filename='mylog.log', filemode='w',format='%(asctime)s - %(message)s', level=logging.DEBUG)

config = configparser.ConfigParser()
config.read('warmme.properties')

for section_name in config.sections():
    print('Section:', section_name)
    print('  Options:', config.options(section_name))
    for key, value in config.items(section_name):
        print('  {} = {}'.format(key, value))
    print()

broker=config['mqtt']['url']
print(broker)
logging.debug(f'Broker url:{broker}')

