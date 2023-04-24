from spi import mcp  
from RPi import GPIO
import time


GPIO.setmode(GPIO.BCM)
servo = 21 
GPIO.setup(servo, GPIO.OUT)
servo_pwm = GPIO.PWM(servo,50)

servo_pwm.start(0)
Spi = mcp(0,0)

try:

    while True:
        potval = Spi.b_in()
        print(f'Potval: {round((potval/1024)*3.3,2)} V')
        print(f'LDR: {round(100-(Spi.b_in(1)/1024)*100,2)} %') #TB
        x = ((potval /1024) * 180) * 12/180
        servo_pwm.ChangeDutyCycle(x)


except KeyboardInterrupt as e:
    print(e)


finally:
    servo_pwm.stop()
    print('final')
    Spi.close()
    GPIO.cleanup()









