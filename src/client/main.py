# Imports
from microbit import *
import radio
radio.on()

while True:
    message = radio.receive()
    
    if button_a.was_pressed() or str(message).upper() == "PRIME":
        radio.send("Primed")
        while True:
            message = radio.receive()
            
            if button_b.was_pressed() or str(message).upper() == "RESET":
                radio.send("Unprimed")
                break
            
            if accelerometer.current_gesture() == "freefall":
                display.show(Image.SAD)
                radio.send("Falling")
                sleep(2500)
                break
            else:
                display.show(Image.HAPPY)
                            
    display.show(Image.ASLEEP)
