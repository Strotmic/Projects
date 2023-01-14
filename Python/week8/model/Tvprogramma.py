from model.Presentator import Presentator

class Tvprogramma:

    def __init__(self, titel, presentator) -> None:
        self.__titel = titel
        self.__presentator = presentator
        self.__is_actief = True

    # ********** property titel - (enkel getter) ***********
    @property
    def titel(self) -> str:
        """ The titel property. """
        return self.__titel
    
    # ********** property presentator - (setter/getter) ***********
    @property
    def presentator(self) -> Presentator:
        """ The presentator property. """
        return self.__presentator
    
    @presentator.setter
    def presentator(self, value: Presentator) -> None:
        if isinstance(value, Presentator):
            self.__presentator = value
        else: self.__presentator = 'ERROR' 
    
    # ********** property is_actief - (setter/getter) ***********
    @property
    def is_actief(self) -> bool:
        """ The is_actief property. """
        return self.__is_actief
    
    @is_actief.setter
    def is_actief(self, value: bool) -> None:
        if isinstance(value, bool):        
            self.__is_actief = value
        else: self.__is_actief = False

    
    def __str__(self) -> str:
        return f'Tv programma: {self.titel} door {self.presentator}'
    
    def __repr__(self) -> str:
        return str(self)
    
    
    
