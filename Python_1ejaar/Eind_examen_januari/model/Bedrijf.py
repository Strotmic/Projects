class Bedrijf:

    def __init__(self, parnaam: str, parstraat: str, parstad: str, parpostcode: str, partelefoon: str, paremailadres: str) -> None:
        self.naam = parnaam
        self.straat = parstraat
        self.stad = parstad
        self.postcode = parpostcode
        self.telefoonnummer = partelefoon
        self.emailadres = paremailadres

    # ********** property naam - (setter/getter) ***********
    @property
    def naam(self) -> str:
        """ The naam property. """
        return self.__naam

    @naam.setter
    def naam(self, value: str) -> None:
        self.__naam = value

    # ********** property straat - (setter/getter) ***********
    @property
    def straat(self) -> str:
        """ The straat property. """
        return self.__straat

    @straat.setter
    def straat(self, value: str) -> None:
        self.__straat = value

    # ********** property stad - (setter/getter) ***********
    @property
    def stad(self) -> str:
        """ The stad property. """
        return self.__stad

    @stad.setter
    def stad(self, value: str) -> None:
        self.__stad = value

    # ********** property postcode - (setter/getter) ***********
    @property
    def postcode(self) -> str:
        """ The postcode property. """
        return self.__postcode

    @postcode.setter
    def postcode(self, value: str) -> None:
        self.__postcode = value

    # ********** property telefoon - (setter/getter) ***********
    @property
    def telefoon(self) -> str:
        """ The telefoon property. """
        return self.__telefoon

    @telefoon.setter
    def telefoon(self, value: str) -> None:
        self.__telefoon = value

    # ********** property emailadres - (setter/getter) ***********
    @property
    def emailadres(self) -> str:
        """ The emailadres property. """
        return self.__emailadres

    @emailadres.setter
    def emailadres(self, value: str) -> None:
        self.__emailadres = value

    def __str__(self) -> str:
        return f"{self.naam} - ({self.stad})" 
    
    def __repr__(self) -> str:
        return f"{self.naam} - ({self.stad})"
