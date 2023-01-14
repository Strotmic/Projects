from math import gcd

class Breuk:

    def __init__(self,teller,noemer) -> None:
        self.teller = teller
        self.noemer = noemer
    
    def __str__(self) -> str:
        return f'Breuk : {self.teller}/{self.noemer}'

    def vereenvoudig(self):
        deler = gcd(self.teller,self.noemer)
        self.teller = self.teller/deler
        self.noemer = self.noemer/deler


    # ********** property teller - (setter/getter) ***********
    @property
    def teller(self) -> float:
        """ The teller property. """
        return self.__teller
    
    @teller.setter
    def teller(self, value: float) -> None:
        self.__teller = value
    
    # ********** property noemer - (setter/getter) ***********
    @property
    def noemer(self) -> float:
        """ The noemer property. """
        return self.__noemer
    
    @noemer.setter
    def noemer(self, value: float) -> None:
        self.__noemer = value
    

    
        