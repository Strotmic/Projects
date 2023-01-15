naam = input('Geef uw naam op: ').lower().strip()
voornaam = input('Geef uw voornaam op: ').upper()
datum = input('Geboortedatum in dd-mm-yyyy: ').lower()

def genereer_passwoord(naam,voornaam,datum):
    return f'{naam[0:3]}{voornaam [0:2]}{datum[3:5]}{datum[-2:]}'

print(genereer_passwoord(naam,voornaam,datum))