import RPi.GPIO as GPIO
import time

# 13,19,26,23,24,25,12,16
pins = [13,6,26,23,24,25,19,16]
# pins = [16,12,25,24,23,26,19,13]
rs = 21
e = 20

def setup():
    GPIO.setmode(GPIO.BCM)
    for i in range(0,8):
        GPIO.setup(pins[i], GPIO.OUT)
    GPIO.setup(rs, GPIO.OUT)
    GPIO.setup(e, GPIO.OUT)

def send_instruction(value):
    GPIO.output(rs, GPIO.LOW)
    GPIO.output(e, GPIO.HIGH)
    set_data_bits(value)
    GPIO.output(e, GPIO.LOW)
    time.sleep(0.01)

def set_data_bits(byte):
    mask = 0x80
    print('-'*20)
    for i in range(8):
        print(byte & (mask >> i))
        GPIO.output(pins[i], byte & (mask >> i))

def send_character(character):
    GPIO.output(rs, GPIO.HIGH)
    
    GPIO.output(e, GPIO.HIGH)
    set_data_bits(character)
    
    GPIO.output(e, GPIO.LOW)
    
    time.sleep(0.2)

def init_LCD():
    send_instruction(0b00111000)
    send_instruction(0b00001111)
    send_instruction(0b00000001)
def write_message(message):
    for char in message[0:16]:
        send_character(ord(char))
    for char in message[16:]:
        move_screen()
        send_character(ord(char))

def move_screen():
    send_instruction(0b00011000)
try:
    setup()
    init_LCD()
    write_message('dikzak')

except KeyboardInterrupt as e:
    print(e)


finally:
    # init_LCD()
    GPIO.cleanup()