from RPi import GPIO
import time
import spidev


GPIO.setmode(GPIO.BCM)
spi = spidev.SpiDev()
spi.open(0, 0) # Bus SPI0, slave op CE 0
spi.max_speed_hz = 10 ** 5 # 100 kHz

commando_byte = 0b1000<<4
kanaal = 1
byte2 = (0b1000 | kanaal) <<4
def spiDef():
    bytes_out = (1,byte2,0)

    # bytes_in = spi.readbytes(n) # leest n bytes en geeft die terug in een `list`

    # spi.writebytes(bytes_out) # verstuurt bytes uit de `list` bytes_out

    bytes_in = spi.xfer(bytes_out) # verstuurt de bytes in `bytes_out` en ontvangt er evenveel in `bytes_in`. # tussen elke byte wordt SS/CE/CS kort gedeactiveerd.
    
    # bytes_in = spi.xfer2(bytes_out) # idem, maar tussen de bytes in blijft SS/CE/CS actief 
    potVal = ((bytes_in[1] &0x03)<<8) | bytes_in[2]
    print(f'potVal:{potVal}')
try:
    while True:
        spiDef()
        time.sleep(0.7)
except KeyboardInterrupt as e:
    print(e)


finally:
    print('final')
    spi.close()
    GPIO.cleanup()