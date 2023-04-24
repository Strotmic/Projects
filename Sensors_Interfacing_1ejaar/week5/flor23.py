from smbus import SMBus
from RPi import GPIO
import time

i2c = SMBus()
i2c.open(1)

waarde=0

a = 0b11111110
b = 0b11111101
c = 0b11111011
d = 0b11110111
e = 0b11101111
f = 0b11011111
g = 0b10111111
h = 0b01111111

list = [a&b&c&d&e&f,b&c,a&b&g&e&d,a&b&g&c&d,f&g&b&c,a&f&g&c&d,a&f&g&c&d&e,a&b&c&f,a&b&c&d&e&f&g,a&b&c&d&g&f]

btn1 = 21
btn2 = 26

def numberDown(pin):
    global waarde
    waarde-=1
    if waarde==-1:
        waarde=9
    i2c.write_byte(0x20,list[waarde])
    return()

def numberUp(pin):
    global waarde
    waarde+=1
    if waarde==10:
        waarde=0
    i2c.write_byte(0x20,list[waarde])
    return()

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(btn1,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(btn2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(btn1, GPIO.FALLING, callback=numberDown, bouncetime=200)
    GPIO.add_event_detect(btn2, GPIO.FALLING, callback=numberUp, bouncetime=200)

try:
    setup()
    try:
        prevWaarde = waarde
        waarde = list.index(i2c.read_byte(0x20))
    except ValueError as e:
        pass
    while True:
        time.sleep(0.1)

except KeyboardInterrupt as e:
    print(e)


finally:
    i2c.close()
    GPIO.cleanup()