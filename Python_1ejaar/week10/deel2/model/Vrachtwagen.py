from model.Voertuig import Voertuig

class Vrachtwagen:

    def __init__(self,id,merk,bouwjaar,kmstand,max_laadvermogen) -> None:
        Voertuig.__init__(self,id,bouwjaar,merk,kmstand)
        self.max_laadvermogen = max_laadvermogen
        self.vracht=0

    # ********** property max_laadvermogen - (setter/getter) ***********
    @property
    def max_laadvermogen(self) -> float:
        """ The max_laadvermogen property. """
        return self.__max_laadvermogen
    
    @max_laadvermogen.setter
    def max_laadvermogen(self, value: float) -> None:
        if isinstance(value,float) or isinstance(value,int):
            self.__max_laadvermogen = value
        else: raise ValueError('Incorrecte lading')
    
    # ********** property vracht - (setter/getter) ***********
    @property
    def vracht(self) -> float:
        """ The vracht property. """
        return self.__vracht
    
    @vracht.setter
    def vracht(self, value: float) -> None:
        if (isinstance(value, float) or isinstance(value,int)) and value <self.max_laadvermogen:
            self.__vracht = value
        else:
            raise ValueError('Incorrecte __vracht')
    
    def __str__(self) -> str:
        return f'{self.merk} {self.bouwjaar}'
    
    def geef_detail_info(self):
        return f'Details over {self.merk} ({self.bouwjaar} \n\t- ID:{self.id} \n\t- Reisbestemming:{self.reisbestemming} \n\t- Max Laadvermogen:{self.max_laadvermogen}\n\t- Gewicht Vracht: {self.vracht}'
    
    
    