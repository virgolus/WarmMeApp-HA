import RPi.GPIO as GPIO
import time

PumpsMapping={
    '1':16, #sala
    '2':20, #notte
    '3':21, #bagno
    '4':19  #laboratorio
}

GPIO.setmode(GPIO.BCM)
for GpioOut in PumpsMapping.values():
    GPIO.setup(GpioOut,GPIO.OUT)
    GPIO.output(GpioOut,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(GpioOut,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(GpioOut,GPIO.LOW)
    time.sleep(0.5)
