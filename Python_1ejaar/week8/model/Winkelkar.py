from typing import List

class Winkelkar:
    def __init__(self) -> None:
        self.__producten = [] 

    # ********** property producten - (enkel getter) ***********
    @property
    def producten(self) -> List[str]:
        return self.__producten

    def __str__(self) -> str:
        return f"De winkelkar bestaat uit {len(self.producten)}: {self.producten}"

    def voeg_product_toe(self, nieuw_product: str) -> None:
        self.__producten.append(nieuw_product)

    def verwijder_product(self, te_verwijderen_product: str) -> None:
        self.__producten.remove(te_verwijderen_product)


