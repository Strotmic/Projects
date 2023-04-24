from RPi import GPIO
import time
import spidev

class mcp:

    def __init__(self, bus=0,device=0, speed=10**5) -> None: #TB
        self.bus =bus
        self.device=device
        self.speed  = speed
        self.setup()
        pass

    def setup(self):
        self.spi = spidev.SpiDev()
        self.spi.open(self.bus, self.device)
        self.spi.max_speed_hz = self.speed
    
    def b_in(self,kanaal=0):
        bytes_out = (1,(0b1000|kanaal)<<4,0)
        bytes_in = self.spi.xfer(bytes_out)
        value = ((bytes_in[1] & 0x03)<<8) | bytes_in[2]
        

        return value

    def close(self):
        self.spi.close()
