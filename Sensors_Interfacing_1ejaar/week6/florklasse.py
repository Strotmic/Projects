import spidev

class Mcp:
    def __init__(self,bus=0,device=0):
        self.bus = bus
        self.device = device
        self.__setup()

    def __setup(self):
        self.spi = spidev.SpiDev()
        self.spi.open(self.bus, self.device) # Bus SPI0, slave op CE 0
        self.spi.max_speed_hz = 10 ** 5 # 100 kHz

    def spiDef(self,kanaal=0):
        bytes_out = (1,(0b1000|kanaal)<<4,0)

        # bytes_in = spi.readbytes(n) # leest n bytes en geeft die terug in een `list`

        # spi.writebytes(bytes_out) # verstuurt bytes uit de `list` bytes_out

        bytes_in = self.spi.xfer(bytes_out) # verstuurt de bytes in `bytes_out` en ontvangt er evenveel in `bytes_in`. # tussen elke byte wordt SS/CE/CS kort gedeactiveerd.
        
        # bytes_in = spi.xfer2(bytes_out) # idem, maar tussen de bytes in blijft SS/CE/CS actief 
        Val = (bytes_in[1] & 0x03)<<8 | bytes_in[2]
        if kanaal==0:
            printVal = (Val/1024)*3.3
        elif kanaal==1:
            printVal = 100-(Val/1024)*100
        
        return printVal
    
    def closespi(self):
        self.spi.close()