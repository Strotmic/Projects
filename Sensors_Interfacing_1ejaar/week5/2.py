from RPi import GPIO
from smbus import SMBus
import time
btn1 = 19
btn2 = 26

btnPrev1=1
btnPrev2=1

byte=0

GPIO.setmode(GPIO.BCM)
GPIO.setup(btn1,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(btn2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#led1 is rood led2 is wit
def led1(pin):
    t = i2c.read_byte(0x20)
    if t & 0x1:
        #als het een 1 is word het nul
        y = t & 0b11111110 #omkeren is & met omgekeerde (de 1 word 0)
        i2c.write_byte(0x20,y)
    else:
        #als het nul is word het 1
        y = t | 0b00000001  # nul word 1
        i2c.write_byte(0x20,y)

def led2(pin):
    t = i2c.read_byte(0x20)
    if t & 0x2:
        #als het een 1 is word het nul
        y = t & 0b11111101
        i2c.write_byte(0x20,y)
    else:
        #als het nul is word het 1
        y = t | 0b00000010
        i2c.write_byte(0x20,y)  

GPIO.add_event_detect(btn1, GPIO.FALLING, callback=led1, bouncetime=200)
GPIO.add_event_detect(btn2, GPIO.FALLING, callback=led2, bouncetime=200)

i2c = SMBus()
i2c.open(1)

#1 is enkel rood
#2 is enkel wit
i2c.write_byte(0x20,0)
try:
    while True:
        time.sleep(1)

except KeyboardInterrupt as e:
    print(e)
finally :
    i2c.write_byte(0x20,355)
    i2c.close()