from gpiozero import PWMLED
from time import sleep

red = PWMLED(27)
try:
    while True:
        red.value = 0  # off
        sleep(1)
        red.value = 0.25  # off
        sleep(1)
        red.value = 0.5  # half brightness
        sleep(1)
        red.value = 0.75  # off
        sleep(1)
        red.value = 1  # full brightness
        sleep(1)
        red.value = 0.75  # off
        sleep(1)
        red.value = 0.5  # half brightness
        sleep(1)
        red.value = 0.25  # off
        sleep(1)
except KeyboardInterrupt:
# exits when you press CTRL+C
    print("ctl+c pressed, existing")

except:
    print("Other error or exception occurred!")

finally:
    red.off()
