from RPi import GPIO
from smbus import SMBus
import time

waarde=0
prevWaarde=0
i2c = SMBus()
i2c.open(1)

btn1=21
btn2=26

GPIO.setmode(GPIO.BCM) 
GPIO.setup((btn1,btn2), GPIO.IN, pull_up_down=GPIO.PUD_UP)

a = 0b11111110
b = 0b11111101
c = 0b11111011
d = 0b11110111
e = 0b11101111
f = 0b11011111
g = 0b10111111
h = 0b01111111

dict = [a&b&c&d&e&f,b&c,a&b&g&e&d,a&b&g&c&d,f&g&b&c,a&f&g&c&d,a&f&g&c&d&e,a&b&c,a&b&c&d&e&f&g,a&b&c&d&g&f]

def omhoog(pin):
    global waarde
    waarde+=1
    if waarde==10:
        waarde=0

def omlaag(pin):
    global waarde
    waarde -=1
    if waarde==-1:
        waarde=9

GPIO.add_event_detect(btn1, GPIO.FALLING, callback=omhoog, bouncetime=200)
GPIO.add_event_detect(btn2, GPIO.FALLING, callback=omlaag, bouncetime=200)

try:
    try:
        prevWaarde = waarde
        waarde = dict.index(i2c.read_byte(0x20))
    except ValueError as e:
        pass
    print(waarde)
    # i2c.write_byte(0x20,dict[waarde])
    while True:
        # byte = i2c.read_byte(0x20)
        # button = byte & 0b10000000
        if waarde!= prevWaarde:
            print(waarde)
            i2c.write_byte(0x20,dict[waarde])
            prevWaarde = waarde     

except KeyboardInterrupt as e:
    print(e)

finally:
     i2c.close()

