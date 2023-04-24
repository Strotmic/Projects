from RPi import GPIO
import time
GPIO.setmode(GPIO.BCM)

led=21
led2=16
led3=12
btn=20

knipper =0

btnstate = 1
btnprevstate =1

GPIO.setup(led,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)
GPIO.setup(led3,GPIO.OUT)
GPIO.setup(btn,GPIO.IN,pull_up_down=GPIO.PUD_UP)

try:
    while True:
        knop_status = GPIO.input(btn)
        if knipper ==0:
            GPIO.output(led,GPIO.HIGH)
        if knipper==1:
            GPIO.output(led,GPIO.LOW)
            GPIO.output(led2,GPIO.HIGH)
            GPIO.output(led3,GPIO.HIGH)
        print(f"De status v/d knop is: {knop_status}")
        #if knop_status:
            #GPIO.output(led, GPIO.HIGH)
        #else:
            #GPIO.output(led, GPIO.LOW)
        if btnstate!=btnprevstate:
            knipper =1
            time.sleep(1)
            
        time.sleep(0.1)

except KeyboardInterrupt as e:
    print(e)
    GPIO.output(led, GPIO.LOW)

finally:
    GPIO.cleanup()
    print("Script has stopped!")


print('hello world')