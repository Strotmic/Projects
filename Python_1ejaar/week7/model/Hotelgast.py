class Hotelgast:

    def __init__(self,naam,voornaam,saldo,ingecheckt) -> None:
        self.naam = naam
        self.voornaam = voornaam
        self.saldo = saldo
        self.ingecheckt = ingecheckt
    
    def __str__(self) -> str:
        if self.ingecheckt==True:
            return f'OK: {self.naam} {self.saldo}'
        else: return f'X: {self.naam} {self.saldo}'

    @property
    def naam(self):
        return self.__naam
    @naam.setter
    def naam(self,value):
        if value != '':
            self.__naam = value
        else:
            self.__naam = 'onbekend'

    @property
    def voornaam(self):
        return self.__voornaam
    @voornaam.setter
    def voornaam(self,value):
        if value != '':
            self.__voornaam = value
        else:
            self.__voornaam = 'onbekend'

    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self,value):
        if value >= 0:
            self.__saldo = value
        else:
            self.__saldo= 0

    @property
    def ingecheckt(self):
        return self.__ingecheckt
    @ingecheckt.setter
    def ingecheckt(self,value):
        if type(value) != type(True) :
            self.__ingecheckt = False
        else:
            self.__ingecheckt= value