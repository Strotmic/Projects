# Tim Bleuze 1MCT3
from typing import Dict, List

dict_aardgasverbruik = {"jan": 18.4, "feb": 15.3, "maa": 12.9, "apr": 7.2, "mei": 3.5,
                        "jun": 1.5, "jul": 1.3, "aug": 1.4, "sep": 2.5, "okt": 6.7, "nov": 12.2, "dec": 17.1}

def controleer_som(dict: dict[str,float]) -> bool:
    resultaat = 0 
    for procent in dict.values():
        resultaat += procent
    if resultaat == 100:
        return True
    else: return False

def geef_maanden_grootverbruik(dict : dict[str,float], grenswaarde:float)->list[str]:
    resultaat = []
    for maand,procent in dict.items():
        if procent > grenswaarde:
            resultaat.append(maand)
    return resultaat

def geef_som_maanden(dict: dict[str,float], list_maandnamen:list[str]) -> int:
    resultaat = 0
    for maand_naam in list_maandnamen:
        resultaat += dict[maand_naam]
    return resultaat

print(f"Is het totaal percentage 100?> {controleer_som(dict_aardgasverbruik)}")
grens = float(input("Geef het min percentage op waarop gefilterd moet worden:> "))

gezochte_maanden = geef_maanden_grootverbruik(dict_aardgasverbruik,grens)
print(f"De maanden met het grootste verbruik zijn: {gezochte_maanden}")

print(f"Ze staan samen in voor een gasverbruik van {geef_som_maanden(dict_aardgasverbruik,gezochte_maanden):.2f}%")
