import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
for i in range(10):
    print("LED On: "+str(i))
    GPIO.output(17,GPIO.HIGH)
    sleep(0.5)
    GPIO.output(17,GPIO.LOW)
    sleep(0.5)    
GPIO.cleanup()

