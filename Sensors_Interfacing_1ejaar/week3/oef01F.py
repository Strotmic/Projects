from RPi import GPIO
import time

GPIO.setmode(GPIO.BCM)

pins= [12,16,20,12]
bits=[]

def setup():
    for i in pins:
        GPIO.setup(i,GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # for i in pins:
    #     bits.append(GPIO.input(i))

    # for i in range(4):
    #     print(f'1: {bits[i]}')

    GPIO.add_event_detect(pins[0],GPIO.BOTH, bouncetime=200)
    GPIO.add_event_detect(pins[0], test)

def test(pin):
    teVersturenByte = 0b0000

    for i in range(4):  
        teVersturenByte = teVersturenByte | ((not GPIO.input(pins[i])) << i )

    print((teVersturenByte))

try:
    setup()
    while True:
        test()
        time.sleep(1)
    
except KeyboardInterrupt as e:
    print(e)

finally:
    GPIO.cleanup()
    print('stop')