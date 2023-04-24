from RPi import GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 16

GPIO.setup(led,GPIO.OUT)

teVersturenByte = 0b10101010
tekst = 'hallo'

def stuur(x):
    for i in range(0,8):
        byte = x & 0x80
        x = x <<1
        print(int(byte/128))
        GPIO.output(led,byte)
        time.sleep(0.5)


try:
    for i in tekst:
        stuur(ord(i))
        print('-'*10)
except KeyboardInterrupt as c:
    print(c)

finally:
    GPIO.cleanup(led)
