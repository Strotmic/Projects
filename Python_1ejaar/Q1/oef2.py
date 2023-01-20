from typing import Dict

# Voor deze en volgende oefening vertrek je van een dictionary met deelnemers aan een miss-verkiezing.  
# De key is de naam van de miss, de value is de postcode.  
# In de broncode vind je twee voorbeelden waarmee je kan testen: 

# • Maak een functie filter_missen_postcode met als parameters: een dictionary met missen en twee postcodes.  
# • In de functie filter_missen_postcode filter je enkel deze missen uit de doorgegeven dictionary waarvan de postcode 
# tussen de twee doorgegeven postcodes valt (grenzen inbegrepen).  
# • Je geeft de namen van de misses in een list terug.  
# • Test uit met bovenstaande dictionaries en print nadien de teruggegeven list af. 

misses_2018 = {"Tine" : 3700, "Anke" : 8700, "Claudia": 8530, "Marijn": 9000, "Sofie": 
2650, "Marie" : 9870, "Leen" : 9000, "Conny" : 2800} 
misses_2019 = {"Marieke" : 8800, "Delfien" : 8500, "Mieke": 8531, "Els": 9070, "Lola": 
2500, "Dolly" : 9999, "Marianne" : 9000, "Claudine" : 2800, "Lies" : 3080, "Jacqueline" : 3720, "Jozefien": 8700} 

# Hier vragen we de 2 waardes op (de grenzen van de destbetreffende provincie)
kleinste = int(input('Geef kleinste postcode op:> '))
grootste = int(input('Geef grootste postcode op:> '))

def filter_missen_postcode(dic : Dict[str, int], start : int, stop : int) -> list:
    returnwaarde = []
    for naam, postcode in dic.items():  # We doorlopen de dictionary
        if postcode >=start and postcode <= stop:   # We gaan na of de postcode van de huidige miss tussen de start en stopwaarde ligt, zo ja dan komt ze uit de opgegeven provincie
            returnwaarde.append(naam)
    return returnwaarde

print(f'Dit zijn de gevonden missen uit 2018 {filter_missen_postcode(misses_2018,kleinste,grootste)}')
print(f'Dit zijn de gevonden missen uit 2019 {filter_missen_postcode(misses_2019,kleinste,grootste)}')


