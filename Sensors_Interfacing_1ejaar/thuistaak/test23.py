import serial
from datetime import datetime
currentDateAndTime = datetime.now()
ser = serial.Serial('/dev/ttyAMA0') # open serial port
print(ser.name) # check which port was really used

now = datetime.now()

current_time = now.strftime("%H:%M")
print((current_time))
prevTime = int(current_time[-1:])
ser.write(current_time.encode(encoding='utf-8'))

try:
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        if(int(current_time[-1:])!=prevTime):
            ser.write(current_time.encode(encoding='utf-8'))
            print((current_time))
        prevTime = int(current_time[-1:])

except KeyboardInterrupt as e:
    print(e)

ser.close()  # close port