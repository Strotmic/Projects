from model.Geboortedatum import Geboortedatum
class Speler:
    ploegnaam = ''
    doelpunten= 0 
    def __init__(self, par_naam: str, par_voornaam: str, par_typespeler: str, par_waarde: int = 0, par_aantal_doelpunten: int = 0, Geboortedatum = Geboortedatum(1,1,2019)) -> None:
        self.naam = par_naam
        self.voornaam = par_voornaam
        self.waarde = par_waarde
        self.type = par_typespeler
        self.__aantal_eigen_doelpunten = par_aantal_doelpunten
        self.geboortedatum = Geboortedatum
        Speler.doelpunten += par_aantal_doelpunten

    def maak_doelpunt(self):
        Speler.doelpunten +=1
        self.__aantal_eigen_doelpunten +=1 
        return self.__aantal_eigen_doelpunten

    def __repr__(self):
        return str(self)
    
    @staticmethod
    def get_doelpunten_saldo_ploeg():
        return f'Het doelpunten saldo van {Speler.ploegnaam} is {Speler.doelpunten}'

    # ********** property naam - (setter/getter) ***********
    @property
    def naam(self) -> str:
        """ The naam property. """
        return self.__naam

    @naam.setter
    def naam(self, value: str) -> None:
        self.__naam = value

    # ********** property voornaam - (setter/getter) ***********
    @property
    def voornaam(self) -> str:
        """ The voornaam property. """
        return self.__voornaam

    @voornaam.setter
    def voornaam(self, value: str) -> None:
        self.__voornaam = value

    # ********** property type - (setter/getter) ***********
    @property
    def type(self) -> str:
        """ The type property. """
        return self.__type

    @type.setter
    def type(self, value: str) -> None:
        self.__type = value

    # ********** property aantal_eigen_doelpunten - (enkel getter) ***********
    @property
    def aantal_eigen_doelpunten(self) -> int:
        """ The aantal_eigen_doelpunten property. """
        return self.__aantal_eigen_doelpunten

    def __str__(self) -> str:
        return f"speler: {self.voornaam}, {self.naam} ({self.waarde}/10) doelpunten: {self.aantal_eigen_doelpunten}"
