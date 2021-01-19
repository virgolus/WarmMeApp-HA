import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

while (True):
    GPIO.output(20, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(21, GPIO.LOW)
    time.sleep(1)
    GPIO.output(20, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(21, GPIO.HIGH)

GPIO.cleanup()