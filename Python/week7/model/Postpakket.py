class Postpakket:
    def __init__(self,omschrijving,breedte,hoogte,diepte) -> None:
        self.__omschrijving = omschrijving
        self.breedte = breedte
        self.hoogte = hoogte
        self.diepte = diepte
    
    def __str__(self) -> str:
        return f'Pakketje: {self.omschrijving} ({self.breedte} cm* {self.hoogte} cm* {self.diepte} cm) '
    # ********** property breedte - (setter/getter) ***********
    @property
    def breedte(self) -> int:
        """ The breedte property. """
        return self.__breedte
    
    @breedte.setter
    def breedte(self, value: int) -> None:
        if value >0:
            self.__breedte = value
        else: self.__breedte = 1
    
    
    @property
    def hoogte(self) -> int:
        """ The hoogte property. """
        return self.__hoogte
    
    @hoogte.setter
    def hoogte(self, value: int) -> None:
        if value >0:
            self.__hoogte = value
        else: self.__hoogte = 1    

    @property
    def diepte(self) -> int:
        """ The diepte property. """
        return self.__diepte
    
    @diepte.setter
    def diepte(self, value: int) -> None:
        if value >0:
            self.__diepte = value
        else: self.__diepte = 1    
    
    # ********** property omschrijving - (enkel getter) ***********
    @property
    def omschrijving(self) -> str:
        """ The omschrijving property. """
        return self.__omschrijving

    # ********** property volume - (enkel getter) ***********
    @property
    def volume(self) -> int:
        """ The volume property. """
        return (self.breedte * self.hoogte * self.diepte)
    
    
    
    