from datetime import datetime


class Persoon:

    # class attributes (géén self!)
    vereniging = "Howest"
    __aantal_personen = 0

    def __init__(self, par_naam: str, par_voornaam: str, par_geboortejaar: int = 2022):
        self.naam = par_naam
        self.voornaam = par_voornaam
        self.geboortejaar = par_geboortejaar
        # Hoera, er is een nieuw object
        Persoon.__aantal_personen += 1

    def __del__(self):
        # Helaas, er is één object verwijderd
        Persoon.__aantal_personen -= 1

    # ********** property naam - (setter/getter) ***********
    @property
    def naam(self) -> str:
        """ The naam property. """
        return self.__naam

    @naam.setter
    def naam(self, value: str) -> None:
        if value != "" or not value.isalpha():
            self.__naam = value
        else:
            self.__naam = None
            raise ValueError("Geen geldige naam!")

    # ********** property voornaam - (setter/getter) ***********
    @property
    def voornaam(self) -> str:
        """ The voornaam property. """
        return self.__voornaam

    @voornaam.setter
    def voornaam(self, value: str) -> None:
        if value != "" and value.isalpha():
            self.__voornaam = value
        else:
            self.__voornaam = None
            raise ValueError("Geen geldige voornaam")

    # ********** property geboortejaar - (setter/getter) ***********
    @property
    def geboortejaar(self) -> int:
        """ The geboortejaar property. """
        return self.__geboortejaar

    @geboortejaar.setter
    def geboortejaar(self, value: int) -> None:
        if isinstance(value,int):
            self.__geboortejaar = value
        else:
            self.__geboortejaar = -1
            raise ValueError("Geen geldig geboortejaar")

    # Calcultated property
    # ********** property leeftijd - (enkel getter) ***********
    @property
    def leeftijd(self) -> int:
        """ The leeftijd property. """
        verschil = datetime.now().year - self.geboortejaar
        return verschil

    def __str__(self) -> str:
        return f"{self.naam.upper()}, {self.voornaam} "

    def __repr__(self) -> str:
        return f"Persoon: {self.naam.upper()} {self.voornaam} ({self.geboortejaar})"


    # equals-operator
    def __eq__(self, other: object) -> bool:
        # print("<EQ-Persoon>")
        if self.naam == other.naam and self.voornaam == other.voornaam and self.geboortejaar == other.geboortejaar:
            return True
        else:
            return False

    # lower-then operator: we overschrijven de < operator
    # sorteren op leeftijd.
    # bij zelfde leeftijd: sorteren op naam
    def __lt__(self, other: object) -> bool:
        if self.leeftijd != other.leeftijd:
            if self.leeftijd < other.leeftijd:
                return True
            else:
                return False
        else:
            if self.naam < other.naam:
                return True
            else:
                return False

    # static-methodes zetten we onderaan
    @staticmethod
    def geef_aantal_personen() -> int:
        return Persoon.__aantal_personen
