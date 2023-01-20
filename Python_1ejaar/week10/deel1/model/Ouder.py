# maak zelf de klasse ouder aan
from model.Persoon import Persoon
from model.Student import Student
class Ouder:

    def __init__(self, parnaam: str, parvoornaam: str,  pargeboortejaar: int = 2022) -> None:
        Persoon.__init__(self,parnaam, parvoornaam, pargeboortejaar)
        self.__studenten = [] 

    def __str__(self) -> str:
        return f'Ouder {super().__str__()}'
    
    def __repr__(self) -> str:
        return f'Ouder {self.naam.upper()}, {self.voornaam} '

    # ********** property studenten - (enkel getter) ***********
    @property
    def studenten(self) -> list:
        """ The studenten property. """
        return self.__studenten
    
    def voeg_student_toe(self, stud):
        l=[]
        for i in self.__studenten:
            l.append(i.studentennummer)
        
        if isinstance(stud,Student) and stud.studentennummer not in l:
            self.__studenten.append(stud)


    def geef_opleidingen_studenten(self):
        l =[]
        for i in self.__studenten:
            if i.opleiding not in l:
                l.append(i.opleiding)
        return l
    
    def geef_info_studenten(self):
        print(f'Ouder {self.naam.upper()}, {self.voornaam} ({self.geboortejaar}) heeft volgende studenten:')
        for i in self.__studenten:
            print(f'Student {i.naam.upper()}, {i.voornaam}, {i.geboortejaar} heeft volgende richting {i.opleiding}')


        











































































































































    