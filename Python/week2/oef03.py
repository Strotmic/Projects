import datetime
year = datetime.date.today().year
month = datetime.date.today().month
jaar = int(input('Wat is uw geboortejaar?: '))
maand = int(input('Wat is de maand?: '))

if year - jaar > 18:
    print('u mag drinken')
elif year - jaar == 18 and maand <= month:
    print('u mag drinken')
else:
    print('u mag niet drinken')


