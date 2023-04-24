from RPi import GPIO
import time
from smbus import SMBus

class LCD:
    def __init__(self, rs, enable, pcf):
        self.rs = rs
        self.enable = enable
        self.pcf = pcf
        GPIO.setup(self.rs, GPIO.OUT)
        GPIO.setup(self.enable, GPIO.OUT)

        time.sleep(0.1)
        self.init_LCD()
    def send_instructGPIOn(self, value):
        # rs laag: voor instructGPIOn
        GPIO.output(self.rs, GPIO.LOW)
        # enable hoog
        GPIO.output(self.enable, GPIO.HIGH)
        self.set_data_bits(value)
        # enable terug laag
        GPIO.output(self.enable, GPIO.LOW)
        time.sleep(0.01)

    # stuur 1 character
    def send_character(self, character):
        # rs hoog: voor data
        GPIO.output(self.rs, GPIO.HIGH)
        # enable hoog
        GPIO.output(self.enable, GPIO.HIGH)
        # data klaarzetten
        self.set_data_bits(character)
        # enable laag
        GPIO.output(self.enable, GPIO.LOW)
        # wait
        time.sleep(0.01)

    # set_data_bits(value)
    def set_data_bits(self, byte):
        self.pcf.write_outputs(byte)

    # write_message(message).
    def write_message(self, message):
        for char in message[:16]:
            self.send_character(ord(char))
        for char in message[16:]:
            self.move_screen()
            self.send_character(ord(char))

    def clear_display(self):
        self.send_instructGPIOn(0b00000001)

    def init_LCD(self):
        self.send_instructGPIOn(0b00111000)
        self.send_instructGPIOn(0b00001111)
        self.clear_display()

    def move_screen(self):
        self.send_instructGPIOn(0b00011000)

    # set cursor
    def set_cursor(self, row, col):
        byte = row << 6 | col
        self.send_instructGPIOn(byte | 128)
    