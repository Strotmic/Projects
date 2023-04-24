# flor degrande
# from MCP3008 import Mcp
# from rgbLedClass import rgbLed
import time
from RPi import GPIO
from subprocess import check_output
from pcf import Pcf8574
from lcd import LCD
# import serial

# setup
# switch = 21
# timesPressed = 0

# ledBlauw = 13
# ledGroen = 19
# ledRood = 26

lcdState=0

# btn1 = 20

i2c = Pcf8574(2,3,0x20)

ips = str(check_output(['ifconfig','wlan0']))
startpos = ips.find("inet")+4
ips = ips[startpos:].split(" ")
ips=ips[1]

# prevTime=''
# prevTimeS=''
# i=0

GPIO.setmode(GPIO.BCM)

# GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(btn1,GPIO.IN, pull_up_down=GPIO.PUD_UP)

# def sendTime():
#     global prevTime
#     t = time.localtime()
#     current_time = time.strftime("%H%M ", t)
#     if current_time!=prevTime:
#         tekst = "a"
#         teversturentekst = tekst.encode(encoding='utf-8')
#         ser.write(teversturentekst) # write a string

#         tekst = f"{current_time}"
#         teversturentekst = tekst.encode(encoding='utf-8')
#         ser.write(teversturentekst) # write a string
#     prevTime=current_time
#     # line = ser.readline().decode('utf-8').rstrip()
#     # print(line)
#     # return(tekst)
#     # time.sleep(5)
    

# def sendSeconds(pin):
#     global prevTimeS
#     global i
#     global prevTime
#     t = time.localtime()
#     # current_time = time.strftime("%M%S ", t)
#     # if current_time!=prevTimeS:
#         # tekst = "a"
#         # teversturentekst = tekst.encode(encoding='utf-8')
#         # ser.write(teversturentekst) # write a string
#     for i in range(0,5):
#         tekst = "a"
#         teversturentekst = tekst.encode(encoding='utf-8')
#         ser.write(teversturentekst) # write a string
#         time.sleep(0.5)
#         t = time.localtime()
#         current_time = time.strftime("%M%S ", t)
#         tekst = f"{current_time}"
#         teversturentekst = tekst.encode(encoding='utf-8')
#         ser.write(teversturentekst) # write a string
#         teversturentekst = tekst.encode(encoding='utf-8')
#         time.sleep(0.5)
#         if i==4:
#             prevTime=''
#             sendTime()
#             return()

# GPIO.add_event_detect(btn1, GPIO.FALLING, callback=sendSeconds, bouncetime=200)

# functie om aantal keer dat de knop ingedrukt is af te printen
# def printSwitchPress(pin):
#     global timesPressed
#     timesPressed+=1
#     print(f'Er is {timesPressed} keer op de joystick gedrukt!')

#     global lcdState
#     global prevValue
#     lcdState+=1
#     prevValue=-1
    

#     print(lcdState)
#     if lcdState>3:
#         lcdState=1

# # event detection voor switch
# GPIO.add_event_detect(switch, GPIO.FALLING, callback=printSwitchPress, bouncetime=300)

try:
    # Spi = Mcp(0,0)
    # rgbLed(ledBlauw,ledRood,ledGroen)
    display = LCD(26,19,i2c)
    # ser = serial.Serial('/dev/ttyS0') # open serial port
    # ser.reset_input_buffer()
    # printSwitchPress(1)
    # ser.readline()
    lcdState =1
    while True:
        # prevValue=-1
        if lcdState==1:
            display.clear_display()
            display.write_message('WLAN0')
            display.set_cursor(1,0)
            display.write_message(f'{ips}')
            lcdState+=1

        # elif lcdState==2:
        #     display.clear_display()
        #     value=Spi.spiDef(1)
        #     numberBlocks=int((value/1024)*16)
        #     for i in range(0,numberBlocks+1):
        #         display.send_character(219)
        #     display.set_cursor(1,0)
        #     display.write_message(f'VRX => ')
        #     # display.write_message(f'{value}')
        #     # value=Spi.spiDef(1)
        #     if value!=prevValue:
        #         display.set_cursor(1,7)
        #         display.write_message(f'{value}')
        #         prevValue=value
            

        
        # elif lcdState==3:
        #     display.clear_display()
        #     value=Spi.spiDef(0)
        #     numberBlocks=int((value/1024)*16)
        #     for i in range(0,numberBlocks+1):
        #         display.send_character(219)
        #     display.set_cursor(1,0)
        #     display.write_message(f'VRY => ')
        #     if value!=prevValue:
        #         display.set_cursor(1,7)
        #         display.write_message(f'{value}')
        #         prevValue=value

        # sendTime()
        # # print(ser.readline())
        # xVal= int((Spi.spiDef(1) / 1024)*100)
        # # print(f'xVal: {xVal}')
        # rgbLed.kleurChangeCycle('ledBlauw',xVal)

        # yVal = int((Spi.spiDef(0) / 1024)*100)
        # # print(f'yVal: {yVal}')
        # rgbLed.kleurChangeCycle('ledRood',yVal)

        # medVal = int((xVal+yVal)/2)
        # rgbLed.kleurChangeCycle('ledGroen',medVal)
        # time.sleep(0.1)

except KeyboardInterrupt as e:
    print(e)


finally:
    print('final')
    # Spi.closespi()
    GPIO.cleanup()
    # ser.close()  # close port