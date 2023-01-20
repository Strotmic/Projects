from model.Persoon import Persoon
from typing import List

class Docent(Persoon):

    def __init__(self, parnaam: str, parvoornaam: str, parpersoneelsnummer: int, pargeboortejaar: int=2022) -> None:
        super().__init__(parnaam, parvoornaam, pargeboortejaar)
        self.personeelsnummer = parpersoneelsnummer
        self.__opleidingen = []  # list: in welke opleidingen geeft hij/zij les?


    # ********** property personeelsnummer - (setter/getter) ***********
    @property
    def personeelsnummer(self) -> int:
        """ The personeelsnummer property. """
        return self.__personeelsnummer
    
    @personeelsnummer.setter
    def personeelsnummer(self, value: int) -> None:
        if isinstance(value,int):
            self.__personeelsnummer = value
        else:
            raise ValueError("Geen geldig personeelsnummer!")
    
    # ********** property opleiding - (enkel getter) ***********
    @property
    def opleiding(self) -> List[str]:
        """ The opleiding property. """
        return self.__opleiding
            

    def geeft_les_in(self, opleiding: str) -> None:
        if not opleiding in self.__opleidingen:
            self.__opleidingen.append(opleiding)
        else:
            raise ValueError("Opleiding is al toegevoegd.")

    def __str__(self) -> str:
        return "Docent " + super().__str__()

