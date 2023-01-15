email = input('Geef een howest email adres op: ')

voornaam = str.title(email[0:email.find('.')])
naam = str.title(email[email.find('.')+1:email.find('@')])
naam = naam.replace('.',' ')
print(f'De naam is {naam} en de voornaam is {voornaam}')