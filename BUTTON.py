from gpiozero import Button
from time import sleep

button = Button(26,pull_up=True)

try:
    while True:
        if button.is_pressed:
            print("Button is pressed")
        else:
            print("Button is not pressed")
            sleep(1)
except KeyboardInterrupt:
# exits when you press CTRL+C
    print("ctl+c pressed, existing")
finally:
    print("exiting")