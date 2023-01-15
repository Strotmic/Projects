import random

class Geboortedatum:
    __aantal_geboortedata = 0
    # Constructor
    def __init__(self, dag,maand,jaar) -> None:
        self.dag = dag
        self.maand = maand
        self.jaar = jaar
        Geboortedatum.__aantal_geboortedata +=1
        pass

    # Properties
    # ********** property dag - (setter/getter) ***********
    @property
    def dag(self) -> int:
        """ The dag property. """
        return self.__dag
    
    @dag.setter
    def dag(self, value: int) -> None:
        if value >0 and value<=31:
            self.__dag = value
        else:
            print('Geen geldige dag')

    # ********** property maand - (setter/getter) ***********
    @property
    def maand(self) -> int:
        """ The maand property. """
        return self.__maand
    
    @maand.setter
    def maand(self, value: int) -> None:
        if value >0 and value<=12:
            self.__maand = value
        else:
            print('Geen geldige maand')
    
    # ********** property jaar - (setter/getter) ***********
    @property
    def jaar(self) -> int:
        """ The jaar property. """
        return self.__jaar
    
    @jaar.setter
    def jaar(self, value: int) -> None:
        if value >1900:
            self.__jaar = value
        else:
            print('Geen geldig jaar')
    
    # ToString
    def __str__(self) -> str:
        return f'{self.dag}/{self.maand}/{self.jaar}'

    # Extra functies

    @staticmethod
    def genereer_willekeurige_verjaardag():
        dag = random.randint(1,31)
        maand = random.randint(1,12)
        jaar = random.randint(1900,2022)
        f = Geboortedatum(dag,maand,jaar)
        return f
    
    @staticmethod
    def genereer_lijst_verjaardagen(lengte):
        l=[]
        for i in range(0,lengte):
            datum = Geboortedatum.genereer_willekeurige_verjaardag()
            l.append(datum)
        return l
    
    def __eq__(self, __o: object) -> bool:
        if self.dag == __o.dag and self.maand == __o.maand and self.jaar == __o.jaar:
            return True
        else: return False

    def __repr__(self):
        return str(self)

    def zelfde_verjaardag(self, object):
        if self.dag == object.dag and self.dag == object.maand:
            return True
        else: return False 
    
    @staticmethod
    def geef_aantal_geboortedatums():
        return Geboortedatum.__aantal_geboortedata

