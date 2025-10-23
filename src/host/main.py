# Imports go at the top
from microbit import *
import radio
radio.on()

# Code in a 'while True:' loop repeats forever
while True:
    display.show(Image.HAPPY)
    if button_a.was_pressed():
        radio.send('prime')
        while True:
            display.show(Image.ASLEEP,delay=100)
            msg = radio.receive()
            if str(msg).upper() == "FALLING":
                display.show(Image.SURPRISED)
                audio.play(Sound.SAD)
                sleep(500)
                radio.send("<3")
                break
            elif button_b.was_pressed():
                radio.send("reset")
                break
            
