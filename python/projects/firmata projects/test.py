from pyfirmata2 import Arduino
from time import sleep
Arduino = Arduino('/dev/ttyACM0')

ledPin = Arduino.get_pin('d:13:o')

while True:
    ledPin.write(1)
    sleep(0.5)
    ledPin.write(0)