from RPi import GPIO 
import time

led_rood = 16
led_rood2=20
led_wit=21
btn = 12
btnprevstate = 1
btnstate=1
prevtime = time.time()
stoptijd = 0

# def setup():
GPIO.setmode(GPIO.BCM) 
GPIO.setup((16, 20, 21, 16), GPIO.OUT) 
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def test(pin):
    global knipper 
    global stoptijd
    if knipper ==1:
            stoptijd += 10
            print('vermeerdert')
    else:
        knipper = 1
        stoptijd = time.time() +10

GPIO.add_event_detect(btn, GPIO.FALLING, callback=test, bouncetime=200)

try:
    knipper = 0
    while True:
        if knipper == 0:
            GPIO.output(led_rood2, GPIO.LOW)
            GPIO.output(led_rood, GPIO.LOW)
            if time.time()>= prevtime + 0.5:
                state = GPIO.input(led_wit)
                state = not state
                GPIO.output(led_wit,state)
                prevtime = time.time()

        elif knipper ==1:
            GPIO.output(led_wit,0)
            if time.time() >= prevtime +0.5:
                state = GPIO.input(led_rood)
                GPIO.output(led_rood2, state)
                GPIO.output(led_rood, not state)
                prevtime = time.time()

            if time.time() >= stoptijd:
                knipper = 0

except KeyboardInterrupt as e:
    print(e)
    GPIO.cleanup((led_rood,led_rood2,led_wit,btn))

GPIO.cleanup((led_rood,led_rood2,led_wit,btn)) 