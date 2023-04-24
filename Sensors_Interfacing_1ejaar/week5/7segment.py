from RPi import GPIO
from smbus import SMBus
import time

waarde=0
i2c = SMBus()
i2c.open(1)
# een= 0b11111001
# twee = 0b01000100
# drie = 0b11010000
# vier=0b10011001
# vijf = 0b10010010
# zes = 0b00000010
# zeven=0b11111000
# acht=0b00000000
# negen=0b10010000

a = 0b11111110
b = 0b11111101
c = 0b11111011
d = 0b11110111
e = 0b11101111
f = 0b11011111
g = 0b10111111
h = 0b01111111

dict = [a&b&c&d&e&f,b&c,a&b&g&e&d,a&b&g&c&d,f&g&b&c,a&f&g&c&d,a&f&g&c&d&e,a&b&c,a&b&c&d&e&f&g,a&b&c&d&g&f]

# for i in range(10):
#     i2c.write_byte(0x20,dict[i])
#     time.sleep(0.1)

# knop uitfilteren met 00000100 als de utkomst 0 of 1 asl knop bv op derde bit zit
#                      00000111
try:
    i2c.write_byte(0x20,dict[waarde])
    while True:
        byte = i2c.read_byte(0x20)
        button = byte & 0b10000000
        if button ==0:
            waarde+=1
            if waarde ==10:
                waarde=0
            i2c.write_byte(0x20,dict[waarde])
            time.sleep(0.5)
                
        

except KeyboardInterrupt as e:
    print(e)

finally:
     i2c.close()

