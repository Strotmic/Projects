#Tim Bleuze 1MCT3
from model.Dier import Dier

class Kennel():

    def __init__(self,id,type,is_gekuist=True) -> None:
        self.__id = id
        self.__type = type
        self.is_gekuist = is_gekuist   
        self.__dieren=[]

    # ********** property aantal_dieren - (enkel getter) ***********
    @property
    def aantal_dieren(self) -> type:
        """ The aantal_dieren property. """
        return len(self.dieren)
    
    
    # ********** property dieren - (enkel getter) ***********
    @property
    def dieren(self) -> list:
        """ The dieren property. """
        return self.__dieren
    
    # ********** property id - (enkel getter) ***********
    @property
    def id(self) -> int:
        """ The id property. """
        return self.__id
    
    # ********** property type - (enkel getter) ***********
    @property
    def type(self) -> str:
        """ The type property. """
        return self.__type
    
    # ********** property is_gekuist - (setter/getter) ***********
    @property
    def is_gekuist(self) -> type:
        """ The is_gekuist property. """
        return self.__is_gekuist
    
    @is_gekuist.setter
    def is_gekuist(self, value: type) -> None:
        if isinstance(value,bool):
            self.__is_gekuist = value
    
    def calculated(self):
        return len(self.dieren)

    def voeg_dier_toe(self, dier):
        for i in (self.dieren):
            if(dier == i):
                raise ValueError('Dit dier bestaat al')
        if isinstance(dier, Dier):
            self.dieren.append(dier)
        else: raise ValueError('Dit is geen correct dier')

    def vind_dier_via_naam(self, naam):
        for i in self.dieren:
            if naam == i.naam:
                return i
        return None

    def __eq__(self, __o: object) -> bool:
        if self.id == __o.id:
            return True

        else: return False
    
    def __lt__(self, o):
        if len(self.dieren) == len(o.dieren):
            return self.id<o.id
        else: return len(self.dieren)< len(o.dieren)

    def __str__(self) -> str:
        return f'kennel {self.id} ({self.type})'

    def __repr__(self) -> str:
        return f'kennel {self.id} ({self.type})'
    