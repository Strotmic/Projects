from model.ProductColor import ProductColor
from typing import List
import logging

class MakeUpProduct:

    # constructor
    def __init__(self, parid: int, parbrand: str, parname: str, parprice: float, parproductlink: str) -> None:
        self.id = parid
        self.name = parname
        self.brand = parbrand
        self.productlink = parproductlink
        self.price = parprice
        self.__colors = []

    # ********** property id - (setter/getter) ***********
    @property
    def id(self) -> int:
        """ The id property. """
        return self.__id

    @id.setter
    def id(self, value: int) -> None:
        if isinstance(value, int) and value > 0:
            self.__id = value
        else:
            logging.error("Invalid ID!")
            raise ValueError("Invalid id!")

    # ********** property brand - (setter/getter) ***********
    @property
    def brand(self) -> str:
        """ The brand property. """
        return self.__brand

    @brand.setter
    def brand(self, value: str) -> None:
        if isinstance(value, str) and value != "":
            self.__brand = value
        else:
            logging.error("INvalid brand")
            raise ValueError("Invalid brand!")

    # ********** property name - (setter/getter) ***********
    @property
    def name(self) -> str:
        """ The name property. """
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if isinstance(value, str) and value != "":
            self.__name = value
        else:
            logging.error("Invalid name")
            raise ValueError("Invalid name!")

    # ********** property price - (setter/getter) ***********
    @property
    def price(self) -> float:
        """ The price property. """
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if isinstance(value, float) and value > 0:
            self.__price = value
        else:
            logging.error("Invalid Price")
            raise ValueError("Invalid price!")

    # ********** property productlink - (setter/getter) ***********
    @property
    def productlink(self) -> str:
        """ The productlink property. """
        return self.__productlink

    @productlink.setter
    def productlink(self, value: str) -> None:
        if isinstance(value, str) and value != "":
            self.__productlink = value
        else:
            logging.error('Invalid productlink')
            raise ValueError("Invalid productlink!")

    # ********** property colors - (enkel getter) ***********
    @property
    def colors(self) -> List[ProductColor]:
        """ The colors property. """
        return self.__colors

    def add_productcolor(self, new_color: ProductColor) -> None:
        if type(new_color) is ProductColor and new_color not in self.__colors:
            self.__colors.append(new_color)

    def __str__(self) -> str:
        return f"{self.name} ({self.brand}) -> Available Colors: {len(self.colors)}"

    def __repr__(self) -> str:
        return f"{self.name}"

    # Extra functies
    # opm: de nieuwe kleur is een object van de klasse ProductColor
    def add_productcolor(self, new_color: ProductColor):
        # controle op het type van het object
        if isinstance(new_color, ProductColor):
            # ok, toevoegen aan mijn list
            self.__colors.append(new_color)
        else:
            # fout teruggeven als er iets anders geprobeerd wordt...
            logging.error('Geen geldige kleurobject')
            raise ValueError("Geen geldig kleurobject")

    # nodig om te kunnen sorteren van een list
    def __lt__(self, other):
        if len(self.colors) < len(other.colors):
            return True
        else:
            return False
