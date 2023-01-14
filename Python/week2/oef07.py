woord1 = input('Geef een 1e woord op: ')
woord2 = input('Geef een 2e woord op: ')

if woord1.lower() == woord2.lower():
    print(f'de woorden {woord1} en {woord2} zijn gelijk')
else:
    print(f'de woorden {woord1} en {woord2} zijn niet gelijk')