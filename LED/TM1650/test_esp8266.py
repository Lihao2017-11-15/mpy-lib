'''
    Four Digit Display demo

    Author: shaoziyang
    Date:   2018.3

    http://www.micropython.org.cn

'''
from machine import I2C,Pin
import time
import FourDigitDisplay

i2c = I2C(freq = 100000,scl=Pin(14), sda=Pin(2))
fdd = FourDigitDisplay.FourDigitDisplay(i2c)

n = 0
while 1:
    fdd.shownum(n)
    n += 1
    time.sleep_ms(1000)
