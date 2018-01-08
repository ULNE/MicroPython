import pyb
import time
while True:
    pyb.LED(3).on()         #LED3 = orange
    time.sleep(1)
    pyb.LED(3).intensity(20)
    time.sleep_ms(500)
