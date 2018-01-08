import pyb
import ssd1306

from pyb import I2C
from machine import Pin

bus = 1
scl = machine.Pin('X9')
sda = machine.Pin('X10')
#i2c = I2C(bus, scl, sda)
#i2c = I2C(bus)

#scl = pyb.Pin('X9',  pyb.Pin.OUT)
#sda = pyb.Pin('X10', pyb.Pin.OUT)
i2c = machine.I2C(bus)


oled = ssd1306.SSD1306_I2C(1, 1, 128, 32, i2c)








#from pyb import I2C

#from pyb import SPI
#spi = SPI(1, SPI.MASTER, baudrate=600000, polarity=1, phase=0, crc=0x7)

#from machine import SPI
#import time
#import sys
#import machine
#import ssd1306
#from ssd1306 import SSD1306_SPI
#ssd = SSD1306_SPI(
#i2c = I2C(sda=Pin(4), scl=Pin(5






#i2c = I2C(1)                         # create on bus 1
#i2c = I2C(1, I2C.MASTER)             # create and init as a master
#i2c.init(I2C.MASTER, baudrate=20000) # init as a master
#i2c.init(I2C.SLAVE, addr=0x42)       # init as a slave with given address
#i2c.deinit()                         # turn off the peripheral

#import machine
#import ssd1306
#i2c = machine.I2C(-1, machine.Pin(5), machine.Pin(4))
#oled = ssd1306.SSD1306_I2C(128, 32, i2c)
