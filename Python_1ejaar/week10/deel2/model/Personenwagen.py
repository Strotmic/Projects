from model.Voertuig import Voertuig

class Personenwagen:

    def __init__(self, id, merk, bouwjaar, kmstand, max_aantal_zitplaatsen) -> None:
       Voertuig.__init__(self, id, bouwjaar, merk, kmstand)
       self.max_aantal_zitplaatsen = max_aantal_zitplaatsen
       self.aantal_personen = 0

    # ********** property max_aantal_zitplaatsen - (setter/getter) ***********
    @property 
    def max_aantal_zitplaatsen(self) -> int:
        """ The max_aantal_zitplaatsen property. """
        return self.__max_aantal_zitplaatsen
    
    @max_aantal_zitplaatsen.setter
    def max_aantal_zitplaatsen(self, value: int) -> None:
        if isinstance(value,int) and value >0:
            self.__max_aantal_zitplaatsen = value
        else: raise ValueError('Error, verkeerde zitplaatse')
    
    # ********** property aantal_personen - (setter/getter) ***********
    @property
    def aantal_personen(self) -> int:
        """ The aantal_personen property. """
        return self.__aantal_personen
    
    @aantal_personen.setter
    def aantal_personen(self, value: int) -> None:
        if isinstance(value,int) and value < self.max_aantal_zitplaatsen:
            self.__aantal_personen = value
        else: raise ValueError('Error, verkeerde zitplaatse')

    # ********** property vrije_plaatsen - (enkel getter) ***********
    @property
    def vrije_plaatsen(self) -> int:
        """ The vrije_plaatsen property. """
        return self.max_aantal_zitplaatsen - self.aantal_personen
    
    

    def __str__(self) -> str:
        return f'{self.merk} {self.bouwjaar}'

    def geef_detail_info(self):
        return f'Details over {self.merk} ({self.bouwjaar} \n\t- ID:{self.id} \n\t- Reisbestemming:{self.reisbestemming} \n\t- Max zitplaatsen:{self.max_aantal_zitplaatsen}\n\t- Vrije zitplaatsen: {self.vrije_plaatsen}'
