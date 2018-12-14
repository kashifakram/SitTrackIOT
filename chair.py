# Add your Python code here. E.g.
from microbit import *
import radio


id = '1'
radio.on()
while True:
    a = int(pin0.read_analog()/4)
    display.scroll(a)
    if a > 5:
        radio.send(id+'1')
    sleep(2000)
