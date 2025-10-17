# Imports
from microbit import *
import radio

radio.on()

while True:
    message = radio.receive()
    
    if accelerometer.current_gesture() == "freefall":
        display.show(Image.SAD)
        radio.send("Falling!")
    else:
        display.show(Image.HAPPY)
    
    if message:
        display.scroll(message)
        sleep(1000)
