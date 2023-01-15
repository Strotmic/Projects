class Winkelkar:
    def __init__(self) -> None:
        self.__producten = []
        
    def __str__(self) -> str:
          return f'De winkelkar bevat {len(self.producten)} producten : {self.producten}'
    # ********** property producten - (enkel getter) ***********
    @property
    def producten(self) -> list:
            """ The producten property. """
            return self.__producten
        
    def voeg_product_toe(self,product):
            self.producten.append(product)
        
    def verwijder_product(self,product):
        if product in self.producten:
            self.producten.remove(product)
        
        