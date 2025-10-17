# Imports
from microbit import *
import radio
from typing import Union
radio.on()

while True:
    message: Union[str,None] = radio.receive()
    
    if button_a.was_pressed() or message.lower() == "PRIME":
        radio.send("Primed.")
        while True:
            if accelerometer.current_gesture() == "freefall":
                display.show(Image.SAD)
                radio.send("Falling!")
                sleep(1000)
                break
            else:
                display.show(Image.HAPPY)
                            
    display.show(Image.ASLEEP)
