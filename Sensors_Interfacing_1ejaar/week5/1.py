from RPi import GPIO
from smbus import SMBus
import time
btn1 = 19
btn2 = 26

btnPrev1=1
btnPrev2=1

Valueled1=0
Valueled2=0

byte=0

GPIO.setmode(GPIO.BCM)
GPIO.setup(btn1,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(btn2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#led1 is rood led2 is wit
def led1(pin):
    global Valueled1
    Valueled1 = not Valueled1
    print('other value for 1')

def led2(pin):
    global Valueled2
    Valueled2 = not Valueled2
    print('other value for 2')

GPIO.add_event_detect(btn1, GPIO.FALLING, callback=led1, bouncetime=200)
GPIO.add_event_detect(btn2, GPIO.FALLING, callback=led2, bouncetime=200)

i2c = SMBus()
i2c.open(1)

#1 is enkel rood
#2 is enkel wit
i2c.write_byte(0x20,355)
print(i2c.read_byte(0x20))
try:
    while True:

        byte = Valueled1 | (Valueled2<<1)
        i2c.write_byte(0x20,byte)

except KeyboardInterrupt as e:
    print(e)
finally :
    i2c.write_byte(0x20,355)
    i2c.close()