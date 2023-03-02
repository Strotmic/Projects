from RPi import GPIO 
import time


led_rood = 16
led_rood2=20
led_wit=21
btn = 12
btnprevstate = 1
btnstate=1

stoptijd = 0

knipper = 0
GPIO.setmode(GPIO.BCM) 

GPIO.setup(9, GPIO.IN) 
GPIO.setup((16, 20, 21, 16), GPIO.OUT) 

GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        GPIO.output(led_wit, GPIO.LOW)
        btnstate = GPIO.input(btn)
        
        if btnstate ==1:
            btnprevstate=1

        if btnstate != btnprevstate:
            if knipper ==1:
                stoptijd += 10
                print(f'de stoptijd is vermeerdert')
            else:
                stoptijd = time.time() +10
                knipper = 1
                print(time.time())
                print(stoptijd)

            btnprevstate = btnstate
            
        time.sleep(0.5)

        if knipper == 0:
            GPIO.output(led_rood2, GPIO.LOW)
            GPIO.output(led_rood, GPIO.LOW)
            GPIO.output(led_wit, GPIO.HIGH)
            time.sleep(1)

        elif knipper ==1:
            GPIO.output(led_rood, GPIO.HIGH)
            GPIO.output(led_rood2, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(led_rood, GPIO.LOW)
            GPIO.output(led_rood2, GPIO.HIGH)

            if time.time() >= stoptijd:
                GPIO.output(led_rood2, GPIO.LOW)
                GPIO.output(led_rood, GPIO.LOW)
                knipper = 0
                print('done')

except KeyboardInterrupt as e:
    print(e)
    GPIO.cleanup((led_rood,led_rood2,led_wit,btn))

GPIO.cleanup((led_rood,led_rood2,led_wit,btn)) 


