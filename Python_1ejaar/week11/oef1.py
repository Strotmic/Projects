import random
from typing import List
import logging

#oef 1
logging.basicConfig(level=logging.DEBUG)
def genereer_even_getallen(aantal: int) -> List[int]:
    even_getallen = []

    while len(even_getallen) != aantal:
        getal = random.randint(0, 1000)
        logging.debug(f"Gekozen getal: {getal}")
        if getal % 2 == 0 and getal not in even_getallen:
            even_getallen.append(getal)
    logging.debug(f"De lijst met even getallen: {even_getallen}")
    return even_getallen

aantal = int(input("Geef een aantal getallen op:> "))
resultaat = genereer_even_getallen(aantal)
print(f"De gekozen even getallen zijn: {resultaat} ")
