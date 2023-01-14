class Bier:

    def __init__(self, naam, brouwerij, alcoholpercentage, kleur) -> None:
        self.naam = naam
        self.brouwerij = brouwerij
        self.alcoholpercentage = alcoholpercentage
        self.kleur = kleur

    def __str__(self) -> str:
        return f'{self.naam} {self.brouwerij} - {self.alcoholpercentage}'
    @property
    def naam(self):
        return self.__naam
    @naam.setter
    def titel(self,value):
        if value != '':
            self.__naam = value
        else:
            self.__naam = 'onbekend'

    @property
    def brouwerij(self):
        return self.__brouwerij
    @brouwerij.setter
    def brouwerij(self,value):
        if value != '':
            self.__brouwerij = value
        else:
            self.__brouwerij = 'onbekend'

    @property
    def kleur(self):
        return self.__kleur
    @kleur.setter
    def kleur(self,value):
        if value != '':
            self.__kleur = value
        else:
            self.__kleur = 'onbekend'

    @property
    def alcoholpercentage(self):
        return self.__alcoholpercentage
    @alcoholpercentage.setter
    def alcoholpercentage(self,value):
        if float(value) > 0 and float(value)<100:
            self.__alcoholpercentage = value
        else:
            self.__alcoholpercentage = -1