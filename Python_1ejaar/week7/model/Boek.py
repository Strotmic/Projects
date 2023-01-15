
class Boek:
    def __init__(self,titel,auteur,uitgeverij,isbn,jaargang=2020) -> None:
        self.titel = titel
        self.auteur = auteur
        self.uitgeverij = uitgeverij
        self.isbn = isbn
        self.jaargang = jaargang

    def __str__(self) -> str:
        return f'“{self.auteur}, {self.titel} ({self.uitgeverij}) *{self.jaargang}*”'

    @property
    def titel(self):
        return self.__titel
    @titel.setter
    def titel(self,value):
        if value != '':
            self.__titel = value
        else:
            print('Lege titel')
            self.__titel = 'empty'

    @property
    def auteur(self):
        return self.__auteur
    @auteur.setter
    def auteur(self,value):
        if value != '':
            self.__auteur = value
        else:
            print('Lege auteur')
            self.__auteur = 'empty'

    @property
    def uitgeverij(self):
        return self.__uitgeverij
    @uitgeverij.setter
    def uitgeverij(self,value):
        if value != '':
            self.__uitgeverij = value
        else:
            print('Lege uitgevrij')
            self.__uitgeverij = 'empty'

    @property
    def isbn(self):
        return self.__isbn
    @isbn.setter
    def isbn(self,value):
        if value != '':
            self.__isbn = value
        else:
            print('Lege isbn')
            self.__isbn = 'empty'

    @property
    def jaargang(self):
        return self.__jaargang
    @jaargang.setter
    def jaargang(self,value):
        if value != '':
            self.__jaargang = value
        else:
            print('Lege jaargang')
            self.__jaargang = 2020