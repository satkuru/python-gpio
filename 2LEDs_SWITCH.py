#should run only from a Raspberry PI
import RPi.GPIO as GPIO
from time import sleep

GREEN=17
RED=27
SWITCH=26
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(GREEN,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(RED,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(SWITCH,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
       if GPIO.input(SWITCH):
          print("Switch is ON, LED ON")
          GPIO.output(GREEN,GPIO.HIGH)
          GPIO.output(RED,GPIO.HIGH)
       else:
          print("Switch is OFF, and Lights too")
          GPIO.output(GREEN,GPIO.LOW)
          GPIO.output(RED,GPIO.LOW)
       sleep(0.1)

finally:
   GPIO.cleanup()


