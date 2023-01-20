from typing import Dict
from oef1 import geef_provincie # importeren deze methode zodat we deze hier kunnen gebruiken

# Maak een functie geef_aantallen_per_provincie met als parameters: een dictionary met missen.  
 
# Deze functie telt per provincie het aantal missen. De provincies met bijhorende aantallen worden in een nieuwe dictionary 
# terug gegeven. Test uit door de teruggegeven dictionary nadien uit te printen. 
 
# Opmerking: maak hier handig gebruik van de functie uit oefening 1 om bij elke miss eerst de provincie te bepalen. 

misses_2018 = {"Tine" : 3700, "Anke" : 8700, "Claudia": 8530, "Marijn": 9000, "Sofie": 
2650, "Marie" : 9870, "Leen" : 9000, "Conny" : 2800} 
misses_2019 = {"Marieke" : 8800, "Delfien" : 8500, "Mieke": 8531, "Els": 9070, "Lola": 
2500, "Dolly" : 9999, "Marianne" : 9000, "Claudine" : 2800, "Lies" : 3080, "Jacqueline" : 3720, "Jozefien": 8700} 


def geef_aantallen_per_provincie(dic : Dict[str,int]) -> Dict[str,int]:
    returndic = {}
    for naam, postcode in dic.items():
        prov = geef_provincie(postcode)   #gebruikt de methode om na te gaan welke provincie de miss van is

        if prov in returndic.keys():  # als deze provincie al in de dict zit dan doen we de waarde van die key +1
            returndic[prov] += 1
        else:                          # als deze er nog niet in zit dan maken we een nieuwe key aan met waarde 1
            returndic[prov] = 1  

    return returndic



# 3b
# Maak een functie geef_aantal_van_een_provincie met als parameters: een dictionary met missen en een provincienaam.  
 
# Deze functie telt per provincie het aantal missen. De provincies met bijhorende aantallen worden in een nieuwe dictionary 
# terug gegeven. Test uit door de teruggegeven dictionary nadien uit te printen. 
 
def geef_aantal_van_een_provincie(dic : Dict[str,int], provnaam: str) -> str:
    provdic = geef_aantallen_per_provincie(dic)
    return provdic[provnaam]                # hier returnen we de waarde van de provincie die als key zit van de methode hierboven

print(f'Aantal missen per prov uit 2019 {geef_aantallen_per_provincie(misses_2019)} ')

provnaam = input('Geef een Vlaamse Provincienaam op: > ')
print(f'Het aantal missen van {provnaam} uit 2018 is {geef_aantal_van_een_provincie(misses_2018, provnaam)}')

