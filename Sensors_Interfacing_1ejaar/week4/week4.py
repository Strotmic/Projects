from RPi import GPIO
import serial
ser = serial.Serial('/dev/ttyAMA0') # open serial port
print(ser.name) # check which port was really used
tekst = "test"
teversturentekst = tekst.encode(encoding='utf-8')
ser.write(teversturentekst) # write a string

btn1 = 20
btn2 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(btn1,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(btn2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def sensor1(pin):
    tekst = "sensor_1"
    teversturentekst = tekst.encode(encoding='utf-8')
    ser.write(teversturentekst) # write a string

def sensor2(pin):
    tekst = "sensor_2"
    teversturentekst = tekst.encode(encoding='utf-8')
    ser.write(teversturentekst) # write a string

GPIO.add_event_detect(btn1, GPIO.FALLING, callback=sensor1, bouncetime=200)
GPIO.add_event_detect(btn2, GPIO.FALLING, callback=sensor2, bouncetime=200)


try:
    while True:
        line = ser.readline()
        print(line)

except KeyboardInterrupt as e:
    print(e)

ser.close()  # close port
