from model.Bedrijf import Bedrijf
from model.Kennel import Kennel

class Dierenasiel(Bedrijf):

    def __init__(self, parnaam: str, parstraat: str, parstad: str, parpostcode: str, partelefoon: str, paremailadres: str, is_vergund=True) -> None:
        super().__init__(parnaam, parstraat, parstad, parpostcode, partelefoon, paremailadres)
        self.is_vergund = is_vergund
        self.__kennels = []

    # ********** property is_vergund - (setter/getter) ***********
    @property
    def is_vergund(self) -> bool:
        """ The is_vergund property. """
        return self.__is_vergund
    
    @is_vergund.setter
    def is_vergund(self, value: bool) -> None:
        if isinstance(value,bool):
            self.__is_vergund = value
        else: raise ValueError('Vergund is geen bool')
    
    # ********** property kennels - (enkel getter) ***********
    @property
    def kennels(self) -> list:
        """ The kennels property. """
        return self.__kennels
    
    # ********** property aantal_dieren - (enkel getter) ***********
    @property
    def aantal_dieren(self) -> type:
        """ The aantal_dieren property. """
        ret = 0
        for i in self.kennels:
            ret+= i.aantal_dieren
        return ret
    
    def voeg_kennel_toe(self, obj):
        for i in self.kennels:
            if i.id == obj.id:
                raise ValueError('Kennel bestaat al')
        if isinstance(obj, Kennel):
            self.kennels.append(obj)
        else: raise ValueError('Gene correte kennel')
    
    def __str__(self) -> str:
        return super().__str__()