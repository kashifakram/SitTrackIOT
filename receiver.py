# Add your Python code here. E.g.
from microbit import *
import radio

uart.init()
radio.on()
while True:
    a = radio.receive()
    if a:
        uart.write(a)
        display.scroll(a)
