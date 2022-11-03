import RPi.GPIO as GPIO
import time

PumpsMapping={
    '1':16, #sala
    '2':20, #notte
    '3':21, #bagno
    '4':19, #laboratorio
    '6':26 #caldaia
}

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for GpioOut in PumpsMapping.values():
    GPIO.setup(GpioOut,GPIO.OUT)
    GPIO.output(GpioOut,GPIO.HIGH)
