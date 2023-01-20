from model.Tvprogramma import Tvprogramma
from model.Presentator import Presentator
import random
class Zender:
    zenders = 0
    def __init__(self,naam,taal) -> None:
        self.__naam = naam
        self.__taal = taal
        self.__programmas = []
        Zender.zenders +=1

    # ********** property naam - (setter/getter) ***********
    @property
    def naam(self) -> str:
        """ The naam property. """
        return self.__naam
    
    @naam.setter
    def naam(self, value: str) -> None:
        if value!= '':
            self.__naam = value
        else: self.__naam = 'error'
    
    # ********** property taal - (setter/getter) ***********
    @property
    def taal(self) -> str:
        """ The taal property. """
        return self.__taal
    
    @taal.setter
    def taal(self, value: str) -> None:
        if value == 'ENG' or value == 'NL' or value=='FR':
            self.__taal = value
        else: self.__taal = 'error'
    
    def __str__(self) -> str:
        return f'{self.naam} -> {self.__programmas}'

    def voeg_programma_toe(self,programma):
        if isinstance(programma, Tvprogramma):
            self.__programmas.append(programma)
        else: print('Foutief prorgamma')

    def zoek_afgelopen(self):
        l=[]
        for i in self.__programmas:
            if i.is_actief == False:
                l.append(i)
        return l
    
    def selecteer_willekeurig_programma(self):
        ran = random.randint(0,len(self.__programmas)-1)
        return self.__programmas[ran]

    def geef_aantal_aangemaakte_zenders():
        return Zender.zenders