import RPi.GPIO as GPIO
from time import sleep

GREEN=17
RED=27
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(GREEN,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(RED,GPIO.OUT,initial=GPIO.LOW)
for i in range(10):
    print("LED On: "+str(i))
    GPIO.output(GREEN,GPIO.HIGH)
    sleep(0.5)
    GPIO.output(GREEN,GPIO.LOW)
    sleep(0.5)    
    GPIO.output(RED,GPIO.HIGH)
    sleep(0.5)
    GPIO.output(RED,GPIO.LOW)
    sleep(0.5)
GPIO.cleanup()

