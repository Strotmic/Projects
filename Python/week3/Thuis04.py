import re
import unidecode
email = unidecode.unidecode(input('Geef een email op: '))
if re.match('^([a-zA-Z.0-9_%-]+[.][a-zA-Z0-9_%-]+@student[.]howest[.]be)$',email):
    print(f'{email} is geldig')
else: print(f'Ongeldig email adres {email}')