import machine
from neopixel import NeoPixel
import time

dElay = 100
pLED = machine.Pin(13, machine.Pin.OUT)
npLED = NeoPixel(pLED, 10)  #8 LED strip
routine1 = (4, 5, 3, 5, 2, 7, 1, 8, 0, 9)
routine2 = (0, 7, 1, 6, 2, 5, 3, 4)
routine3 = range(10)

while 1:
    for i in routine3:
        npLED[i] = (20, 25 * i, 250 - 25 * i)
        npLED.write()
        time.sleep_ms(dElay)
        npLED[i] = (0, 0, 0)
        npLED.write()
    for i in range(8, 0, -1):
        npLED[i] = (20, 25 * i, 250 - 25 * i)
        npLED.write()
        time.sleep_ms(dElay)
        npLED[i] = (0, 0, 0)
        npLED.write()
