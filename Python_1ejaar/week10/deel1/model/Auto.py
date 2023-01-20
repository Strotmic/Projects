from model.Persoon import Persoon
# from .Persoon import Persoon                  #kan ook


class Auto:

    def __init__(self, par_nummerplaat: str, par_eigenaar: Persoon) -> None:
        self.nummerplaat = par_nummerplaat
        self.eigenaar = par_eigenaar


    # ********** property nummerplaat - (setter/getter) ***********
    @property
    def nummerplaat(self) -> str:
        """ The nummerplaat property. """
        return self.__nummerplaat
    
    @nummerplaat.setter
    def nummerplaat(self, value: str) -> None:
        if value != "":
            self.__nummerplaat = value
        else:
            raise ValueError("Geen geldige waarde voor nummerplaat!")

    # ********** property egenaar - (setter/getter) ***********
    @property
    def egenaar(self) -> Persoon:
        """ The egenaar property. """
        return self.__egenaar
    
    @egenaar.setter
    def egenaar(self, value: Persoon) -> None:
        if isinstance(value,Persoon):
            self.__egenaar = value
        else:
            raise ValueError("Geen geldige eigenaar: moet een object van de klasse Persoon zijn!")

    def __str__(self) -> str:
        return f"Voertuig met kenteken {self.nummerplaat} heeft als eigenaar: {self.eigenaar}"
