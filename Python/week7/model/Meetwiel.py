from math import pi

class Meetwiel:
    
    def __init__(self,straal,omwentelingen=0):
        self.straal =straal
        self.omwentelingen = omwentelingen
    
    def __str__(self) -> str:
        return f'Meetwiel met straal {self.straal} en omwentelingen {self.omwentelingen}'
    # ********** property straal - (setter/getter) ***********
    @property
    def straal(self) -> float:
        """ The straal property. """
        return self.__straal
    
    @straal.setter
    def straal(self, value: float) -> None:
        self.__straal = value

    # ********** property omwentelingen - (setter/getter) ***********
    @property
    def omwentelingen(self) -> float:
        """ The omwentelingen property. """
        return self.__omwentelingen
    
    @omwentelingen.setter
    def omwentelingen(self, value: float) -> None:
        self.__omwentelingen = value
    
    # ********** property omtrek - (enkel getter) ***********
    @property
    def omtrek(self) -> float:
        """ The omtrek property. """
        return (self.__straal + self.__straal) * pi
    
    # ********** property afstand - (enkel getter) ***********
    @property
    def afgelegde_afstand(self) -> float:
        """ The afstand property. """
        return self.omtrek * self.__omwentelingen
    
    
    
    
    
    
    