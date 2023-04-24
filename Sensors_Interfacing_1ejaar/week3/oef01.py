from RPi import GPIO
import time

GPIO.setmode(GPIO.BCM)

pin1 = 12
pin2 = 16
pin4 = 20
pin8 = 21

pins = [12,16,20,21]

for i in pins:
    GPIO.setup(i,GPIO.IN, pull_up_down=GPIO.PUD_UP)
def byte():
    bit1 = GPIO.input(pin1)
    bit2 = GPIO.input(pin2)
    bit4 = GPIO.input(pin4)
    bit8 = GPIO.input(pin8)

    # print(f'1: {bit1}')
    # print(f'2: {bit2}')
    # print(f'4: {bit4}')
    # print(f'8: {bit8}')

    teVersturenByte = 0b0000
    print(bin(teVersturenByte))
    teVersturenByte = teVersturenByte | 1-bit8
    teVersturenByte = teVersturenByte<<1 | 1-bit4
    teVersturenByte = teVersturenByte<<1 | 1-bit2
    teVersturenByte = teVersturenByte<<1 | 1-bit1
    time.sleep(1)
    print(bin(teVersturenByte))
    print((teVersturenByte))
    return()
try:
    while True:
        byte()

except KeyboardInterrupt as e:
    print(e)

finally:
    GPIO.cleanup()
    print("Script has stopped!")



