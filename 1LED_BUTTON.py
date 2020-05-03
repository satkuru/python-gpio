from gpiozero import LED,Button
from signal import pause

red = LED(27)
button = Button(26)

button.when_pressed = red.on
button.when_released = red.off

pause()