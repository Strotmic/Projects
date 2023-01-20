from model.Persoon import Persoon


class Student(Persoon):

    def __init__(self, parnaam: str, parvoornaam: str, parstudentennummer: int, paropleiding: str, pargeboortejaar: int=2022) -> None:
        Persoon.__init__(self, parnaam, parvoornaam, pargeboortejaar)
        # super().__init__(parnaam, parvoornaam, pargeboortejaar)
        self.studentennummer = parstudentennummer
        self.opleiding = paropleiding


    # ********** property studentennummer - (setter/getter) ***********
    @property
    def studentennummer(self) -> int:
        """ The studentennummer property. """
        return self.__studentennummer
    
    @studentennummer.setter
    def studentennummer(self, value: int) -> None:
        if isinstance(value,int) and value > 0:
            self.__studentennummer = value
        else:
            raise ValueError("Geen geldig studentennummer!")
    

    # ********** property opleiding - (setter/getter) ***********
    @property
    def opleiding(self) -> str:
        """ The opleiding property. """
        return self.__opleiding
    
    @opleiding.setter
    def opleiding(self, value: str) -> None:
        if isinstance(value,str) and value != "":
            self.__opleiding = value
        else:
            raise ValueError("Geen geldige opleiding!")
    

    def __str__(self) -> str:
        return f"Student {super().__str__()}"

    def __repr__(self) -> str:
        return f"Student {self.naam} {self.voornaam} ({self.leeftijd})"

    def __eq__(self, other: object) -> bool:
        # print("<eq - Student>")
        if self.studentennummer == other.studentennummer:
            return True
        else:
            return False
