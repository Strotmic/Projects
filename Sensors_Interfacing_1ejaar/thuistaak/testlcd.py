from RPi import GPIO
from lcd import LCD
from pcf import Pcf8574
a=1

GPIO.setmode(GPIO.BCM)
i2c = Pcf8574(2,3,0x20)
display = LCD(26,20,i2c)
try:
    while True:
        if a==1:

            display.clear_display()
            display.write_message('b')
            display.clear_display()
            display.write_message('test')
            display.clear_display()
            display.send_character(ord('a'))
            a+=1
            


except KeyboardInterrupt as e:
    print(e)

finally:

    GPIO.cleanup()

    exit()