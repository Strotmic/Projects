from RPi import GPIO
import time
import spidev


GPIO.setmode(GPIO.BCM)
spi = spidev.SpiDev()
spi.open(0, 0) # Bus SPI0, slave op CE 0
spi.max_speed_hz = 10 ** 5 # 100 kHz

kanaal = 0
def spiDef(kanaal):
    bytes_out = (1,(0b1000|kanaal)<<4,0)

    bytes_in = spi.xfer(bytes_out) # verstuurt de bytes in `bytes_out` en 
    
    Val = ((bytes_in[1] &0x03)<<8) | bytes_in[2]

    return Val
try:
    while True:
        print(f'POT {spiDef(0)}')
        
        time.sleep(0.7)
        print(f'Licht {spiDef(1)}')
        
except KeyboardInterrupt as e:
    print(e)


finally:
    print('final')
    spi.close()
    GPIO.cleanup()