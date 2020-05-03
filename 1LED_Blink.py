from gpiozero import LED
from signal import pause

red = LED(27)
try:
    while True:
        red.blink()
        pause()
except KeyboardInterrupt:
# exits when you press CTRL+C
    print("ctl+c pressed, existing")

except:
    print("Other error or exception occurred!")

finally:
    red.off()
