class Bier:

    # Constructor
    def __init__(self, parnaam, parbrouwerij, paralcoholpercentage, parkleur):
        # hieronder maken we gebruik van de properties!
        self.naam = parnaam
        self.brouwerij = parbrouwerij
        self.alcoholpercentage = paralcoholpercentage
        self.kleur = parkleur

    # ********** property naam - (setter/getter) ***********
    @property
    def naam(self):
        return self.__naam.upper()

    @naam.setter
    def naam(self, value):
        if isinstance(value,str) and value != "":
            self.__naam = value
        else:
            raise ValueError('geen geldige invoer')

    # ********** property brouwerij - (setter/getter) ***********
    @property
    def brouwerij(self):
        return self.__brouwerij

    @brouwerij.setter
    def brouwerij(self, value):
        if isinstance(value,str) and value != "":
            self.__brouwerij = value
        else:
            raise ValueError('geen geldige invoer')

    # ********** property alcoholpercentage - (setter/getter) ***********

    @property
    def alcoholpercentage(self):
        return self.__alcoholpercentage

    @alcoholpercentage.setter
    def alcoholpercentage(self, value):
        if isinstance(value, float) and value >= 0 and value <= 100:
            self.__alcoholpercentage = value
        else:
            raise ValueError('geen geldige invoer')

    # ********** property kleur - (setter/getter) ***********
    @property
    def kleur(self):
        return self.__kleur

    @kleur.setter
    def kleur(self, value):
        if isinstance(value,str) and value != "":
            self.__kleur = value
        else:
            raise ValueError('geen geldige invoer')

    # toString
    def __str__(self):
        return f"{self.naam} {self.brouwerij} - {self.alcoholpercentage}"
    
    def __repr__(self) -> str:
        return str(self)

    def __lt__(self, o):
        return self.alcoholpercentage < o.alcoholpercentage
