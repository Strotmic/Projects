from RPi import GPIO
import time

led = 21

GPIO.setmode(GPIO.BCM)

GPIO.setup(led, GPIO.OUT)
led_wpm = GPIO.PWM(led,1000)

led_wpm.start(10)

time.sleep(5)

led_wpm.ChangeDutyCycle(100)

time.sleep(5)

led_wpm.ChangeDutyCycle(1)

time.sleep(5)

led_wpm.stop()

GPIO.cleanup()