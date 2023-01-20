# Tim Bleuze 1MCT3
from typing import List

def mag_de_verwarming_aan(maandnummer : int, temp_buiten: float) -> str:
    list_maanden_verwarming_aan = [11,12,1,2]
    if maandnummer in list_maanden_verwarming_aan and temp_buiten < 16:
        return 'Verwarming aan!'
    else: return 'Verwarming uit!'

temp_buiten = float(input(f"Wat is de buitentemperatuur?:> "))
maandnummer = int(input("Geef het maandnummer [1-12] op:> "))
print(f"Mag de verwarming aan?> {mag_de_verwarming_aan(maandnummer,temp_buiten)}")

import random
def simuleer_temperaturen_maand(dagen : int, min : float, max : float) -> list:
    l = []
    for i in range(dagen):
        l.append(random.randint(min,max))
    return l

def tel_verwarmings_dagen(maandnummer : int, list_temp: list[int]) -> int:
    count=0
    for temp in list_temp:
        if mag_de_verwarming_aan(maandnummer, temp) == 'Verwarming aan!':
            count+=1
    return count
    

list_temp_oktober = simuleer_temperaturen_maand(31, 5, 22)
print(f"De temperaturen in de maand oktober zijn: {list_temp_oktober}")
list_temp_november = simuleer_temperaturen_maand(30, -5, 20)
print(f"De temperaturen in de maand november zijn: {list_temp_november}")
list_temp_december = simuleer_temperaturen_maand(31, -10, 16)
print(f"De temperaturen in de maand december zijn: {list_temp_december}")

print(f"Het aantal dagen in de maand oktober dat de verwarming aanstaat, bedraagt: {tel_verwarmings_dagen(10,list_temp_oktober)}.")
print(f"Het aantal dagen in de maand november dat de verwarming aanstaat, bedraagt: {tel_verwarmings_dagen(11,list_temp_november)}.")
print(f"Het aantal dagen in de maand december dat de verwarming aanstaat, bedraagt: {tel_verwarmings_dagen(12,list_temp_december)}.")

