class Auto:
    def __init__(self,merk,model,kleur='grijs',brandstof='diesel'):
        self.merk = merk
        self.model = model
        self.kleur = kleur
        self.brandstof = brandstof
        self.kmstand = 0
    
    def __str__(self) -> str:
        return f'{self.merk} ({self.model} kleur: {self.kleur})'

    def maak_lawaai(self):
        if self.brandstof=='diesel':
            return 'bwaahrooh'
        elif self.brandstof=='benzine':
            return 'swoooashj'
        elif self.brandstof=='elektrisch':
            return 'ssssssssst'
        else: return 'panne'
    
    def rijden(self,afstand):
        self.kmstand += afstand
    # ********** property merk - (setter/getter) ***********
    @property
    def merk(self) -> str:
        """ The merk property. """
        return self.__merk
    
    @merk.setter
    def merk(self, value: str) -> str:
        self.__merk = value

    # ********** property model - (setter/getter) ***********
    @property
    def model(self) -> str:
        """ The model property. """
        return self.__model
    
    @model.setter
    def model(self, value: str) -> None:
        self.__model = value
    
    # ********** property kleur - (setter/getter) ***********
    @property
    def kleur(self) -> str:
        """ The kleur property. """
        return self.__kleur
    
    @kleur.setter
    def kleur(self, value: str) -> None:
        self.__kleur = value
    
    # ********** property brandstof - (setter/getter) ***********
    @property
    def brandstof(self) -> str:
        """ The brandstof property. """
        return self.__brandstof
    
    @brandstof.setter
    def brandstof(self, value: str) -> None:
        self.__brandstof = value
    
    
    
    
