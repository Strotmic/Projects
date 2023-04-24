# flor degrande
from florklasse import Mcp
import time
from RPi import GPIO

GPIO.setmode(GPIO.BCM)
Spi = Mcp(0,0)

GPIO.setup(21, GPIO.OUT)
servo = GPIO.PWM(21, 50)
servo.start(0)
try:
    while True:
        ldrVal=Spi.spiDef(1)
        print(f'ldrVal: {ldrVal}')
        
        potVal = Spi.spiDef(0)
        print(f'potVal: {potVal}')
        degree = (potVal / 3.3)*180
        degree = (degree - 0) * (10-0) / 180 + 0
        print(degree)
        servo.ChangeDutyCycle(degree)

except KeyboardInterrupt as e:
    print(e)


finally:
    servo.stop()
    print('final')
    Spi.closespi()
    GPIO.cleanup()