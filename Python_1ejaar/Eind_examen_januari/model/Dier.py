# Tim Bleuze 1MCT3

from datetime import datetime

class Dier():

    def __init__(self, naam,geboortedatum,inschrijvingsdatum,ras,geslacht,gecastreerd) -> None:
        self.naam = naam
        self.geboortedatum = geboortedatum
        self.inschrijvingsdatum = inschrijvingsdatum
        self.__ras = ras 
        self.geslacht = geslacht
        self.gecastreerd = gecastreerd
    
    # ********** property naam - (setter/getter) ***********
    @property
    def naam(self) -> str:
        """ The naam property. """
        return self.__naam
    
    @naam.setter
    def naam(self, value: str) -> None:
        if isinstance(value,str) & (str !=''):
            self.__naam = value
        else: raise ValueError('Foutieve naam')
    
    # ********** property geboortedatum - (setter/getter) ***********
    @property
    def geboortedatum(self) -> datetime:
        """ The geboortedatum property. """
        return self.__geboortedatum
    
    @geboortedatum.setter
    def geboortedatum(self, value: datetime) -> None:
        if isinstance(value,datetime) & (value!=''):
            self.__geboortedatum = value
        else: raise ValueError('foutieve datum (geboorte)')
    
    # ********** property inschrijvingsdatum - (setter/getter) ***********
    @property
    def inschrijvingsdatum(self) -> datetime:
        """ The inschrijvingsdatum property. """
        return self.__inschrijvingsdatum
    
    @inschrijvingsdatum.setter
    def inschrijvingsdatum(self, value: datetime) -> None:
        if isinstance(value,datetime):
            self.__inschrijvingsdatum = value
        else: raise ValueError('Verkeerde datum (inschrijving)')
    
    # ********** property ras - (setter/getter) ***********
    @property
    def ras(self) -> str:
        """ The ras property. """
        return self.__ras
    

    # ********** property geslacht - (setter/getter) ***********
    @property
    def geslacht(self) -> str:
        """ The geslacht property. """
        return self.__geslacht.upper()
    
    @geslacht.setter
    def geslacht(self, value: str) -> None:
        if (value == 'v') | (value =='m'):
            self.__geslacht = value
        else: raise ValueError('Verkeerd geslacht')
    
    # ********** property gecastreerd - (setter/getter) ***********
    @property
    def gecastreerd(self) -> bool:
        """ The gecastreerd property. """
        return self.__gecastreerd
    
    @gecastreerd.setter
    def gecastreerd(self, value: bool) -> None:
        if isinstance(value,bool):
            self.__gecastreerd = value
        else: raise ValueError('verkeerde waarde gecastreerd')
    
    def __eq__(self, __o: object) -> bool:
        if (self.naam == __o.naam) & (self.geboortedatum == __o.geboortedatum):
            return True
        else: return False

    def __lt__(self,obj):
        return self.geboortedatum > obj.geboortedatum

    def __str__(self) -> str:
        return f'{self.naam} ({self.ras})'
    
    def __repr__(self) -> str:
        return f'{self.naam}'