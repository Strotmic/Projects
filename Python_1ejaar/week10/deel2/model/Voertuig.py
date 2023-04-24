class Voertuig:
    __aantal_voertuigen =0
    def __init__(self, id,bouwjaar,merk,kmstand):
        self.id=id
        self.bouwjaar = bouwjaar
        self.merk = merk
        self.kmstand = kmstand
        self.reisbestemming = ''
        Voertuig.__aantal_voertuigen += 1

    @staticmethod
    def geef_aantal_voertuigen():
        return Voertuig.__aantal_voertuigen
    # ********** property id - (enkel getter) ***********
    @property
    def id(self) -> int:
        """ The id property. """
        return self.__id
    
    # ********** property merk - (enkel getter) ***********
    @property
    def merk(self) -> str:
        """ The merk property. """
        return self.__merk.upper()
    
    # ********** property bouwjaar - (enkel getter) ***********
    @property
    def bouwjaar(self) -> int:
        """ The bouwjaar property. """
        return self.__bouwjaar
    
    # ********** property kmstand - (setter/getter) ***********
    @property
    def kmstand(self) -> float:
        """ The kmstand property. """
        return self.__kmstand
    
    @kmstand.setter
    def kmstand(self, value: float) -> None:
        if isinstance(value,float):
            self.__kmstand = value
        else: raise ValueError('Ongeldeige kmafstand')

    # ********** property reisbestemming - (setter/getter) ***********
    @property
    def reisbestemming(self) -> str:
        """ The reisbestemming property. """
        return self.__reisbestemming
    
    @reisbestemming.setter
    def reisbestemming(self, value: str) -> None:
        if isinstance(value,str) or value =='':
            self.__reisbestemming = value
        else: raise ValueError('Niet geldige bestemming')
    
    def __eq__(self, __o: object) -> bool:
        if self.id == __o.id:
            return True
        else: return False
    
    def __lt__(self,o):
        return self.kmstand < o.kmstand

    def __str__(self) -> str:
        return f'Auto met id {self.id} en merk {self.merk} en bouwjaar {self.bouwjaar} heeft {self.kmstand} kilometers en bestemming: {self.reisbestemming}'
    
    def __repr__(self) -> str:
        return self.__str__()
    
    
    

