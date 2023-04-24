from RPi import GPIO
from spi import mcp  
import time

rood = 12
blauw=19
groen=13

GPIO.setmode(GPIO.BCM) 

GPIO.setup(rood, GPIO.OUT)
GPIO.setup(groen, GPIO.OUT)
GPIO.setup(blauw, GPIO.OUT)
rood_pwm = GPIO.PWM(rood,1000)
blauw_pwm = GPIO.PWM(blauw,1000)
groen_pwm = GPIO.PWM(groen,1000)

try:
    GPIO.output(rood,GPIO.LOW)
    GPIO.output(blauw,GPIO.HIGH)
    led_wpm.start(0)
    GPIO.output(groen,GPIO.HIGH)
    while True:

        led_wpm.ChangeDutyCycle(99)

        time.sleep(5)

except KeyboardInterrupt as e:
    print(e)

finally:
    led_wpm.stop()
    GPIO.cleanup()
