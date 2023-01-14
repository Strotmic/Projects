class Hotelgast:
    def __init__(self, parnaam: str, parvoornaam: str, parsaldo: float = 0, paris_ingecheckt: bool = False) -> None:
        self.naam = parnaam
        self.voornaam = parvoornaam
        self.saldo = parsaldo
        self.is_ingecheckt = paris_ingecheckt
    
    def __eq__(self, __o) -> bool:
        
        if self.naam == __o.naam and self.voornaam == __o.voornaam:
            return True
        else: return False

    # ********** property naam - (setter/getter) ***********
    @property
    def naam(self) -> str:
        """ The naam property. """
        return self.__naam

    @naam.setter
    def naam(self, value: str) -> None:
        if value != "":
            self.__naam = value
        else:
            self.__naam = "ONBEKEND"

    # ********** property voornaam - (setter/getter) ***********
    @property
    def voornaam(self) -> str:
        """ The voornaam property. """
        return self.__voornaam

    @voornaam.setter
    def voornaam(self, value: str) -> None:
        if value != "":
            self.__voornaam = value
        else:
            self.__voornaam = "ONBEKEND"

    # ********** property saldo - (setter/getter) ***********
    @property
    def saldo(self) -> float:
        """ The saldo property. """
        return self.__saldo

    @saldo.setter
    def saldo(self, value: float) -> None:
        if isinstance(value, float) and value >= 0:
            self.__saldo = value
        else:
            self.__saldo = 0

    # ********** property is_ingechekt - (setter/getter) ***********

    @property
    def is_ingechekt(self) -> bool:
        """ The is_ingechekt property. """
        return self.__is_ingecheckt

    @is_ingechekt.setter
    def is_ingechekt(self, value: bool) -> None:
        if isinstance(value, bool):
            self.__is_ingecheckt = value
        else:
            self.__is_ingecheckt = False

    def __str__(self) -> str:
        if self.is_ingecheckt == True:
            return f"OK: {self.naam} - {self.saldo} euro"
        else:
            return f"X: {self.voornaam} {self.naam}"
