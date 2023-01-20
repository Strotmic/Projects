class Presentator:

    def __init__(self,naam,voornaam) -> None:
        self.__naam = naam
        self.__voornaam = voornaam

    # ********** property naam - (setter/getter) ***********
    @property
    def naam(self) -> str:
        """ The naam property. """
        return self.__naam
    
    @naam.setter
    def naam(self, value: str) -> None:
        if value == '':
            print('Foutieve naam')
            self.__naam = 'Onbekend'
        else:
            self.__naam = value
    
    # ********** property voornaam - (setter/getter) ***********
    @property
    def voornaam(self) -> str:
        """ The voornaam property. """
        return self.__voornaam
    
    @voornaam.setter
    def voornaam(self, value: str) -> None:
        if value == '':
            print('Foutieve voornaam')
            self.__voornaam = 'Onbekend'
        else:
            self.__voornaam = value
    
    def __str__(self) -> str:
        return f'presentator: {self.naam}, {self.voornaam}'
    
    def __eq__(self, __o: object) -> bool:
        if self.naam == __o.naam and self.voornaam == __o.voornaam:
            return True
        else: return False
    