import logging

class ProductColor:

    # constructor
    def __init__(self, parcolorname: str, parhexvalue: str) -> None:
        self.colorname = parcolorname
        self.hexvalue = parhexvalue

    # properties
    # ********** property colorname - (setter/getter) ***********
    @property
    def colorname(self) -> str:
        """ The colorname property. """
        return self.__colorname

    @colorname.setter
    def colorname(self, value: str) -> None:
        if isinstance(value, str) and value != "":
            self.__colorname = value
        else:
            self.__colorname = None
            logging.error('Foutmelding')
            raise ValueError(f"Foutmelding: foutieve kleurnaam: {value}")

    # ********** property hexvalue - (setter/getter) ***********
    @property
    def hexvalue(self) -> str:
        """ The hexvalue property. """
        return self.__hexvalue

    @hexvalue.setter
    def hexvalue(self, value: str) -> None:
        if isinstance(value, str) and value != "":
            self.__hexvalue = value
        else:
            self.__hexvalue = None
            logging.error("Foutmelding foutieve hex value")
            raise ValueError(f"Foutmelding: foutieve hex-value: {value}")

    # tosString
    def __str__(self) -> str:
        return f"{self.colorname}"

    # representation-methode (afprinten in een list)
    def __repr__(self) -> str:
        return f"{self.colorname}"

    # Extra functies
    # de equals-methode (==) --> nodig om te kijken of 2 objecten aan elkaar gelijk zijn
    def __eq__(self, other: object) -> bool:
        if self.colorname == other. colorname and self.hexvalue == other.hexvalue:
            return True
        else:
            return False
