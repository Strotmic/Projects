from smbus import SMBus
from RPi import GPIO
import time

i2c = SMBus()
i2c.open(1)

state1 = 0
state2 = 0
btn1 = 19
btn2 = 26

def test1(pin):
    print("hello world 1")
    byte = i2c.read_byte(0x20)
    state1 = (byte>>0) & 1
    state1 = not state1
    return()

def test2(pin):
    print("hello world 2")
    byte = i2c.read_byte(0x20)
    state2 = (byte>>1) & 1
    state2 = not state2
    return()

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(btn1,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(btn2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(btn1, GPIO.FALLING, callback=test1, bouncetime=200)
    GPIO.add_event_detect(btn2, GPIO.FALLING, callback=test2, bouncetime=200)

try:
    while True:
        byteTeVersturen = state1 | (state2 << 1)
        i2c.write_byte(0x20,byteTeVersturen)
        time.sleep(0.1)

except KeyboardInterrupt as e:
    print(e)


finally:
    i2c.close()
    GPIO.cleanup()