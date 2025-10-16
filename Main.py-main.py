# Imports
from microbit import *

while True:
    if accelerometer.current_gesture():
        print("oh dear god")
    else:
        print("were fine")
