def maak_verwelkoming_klas(naam, klas='1MCT'):
    if klas == '':
        klas = '1MCT'
    return(f'Welkom {naam} in groep {klas}')

if __name__ == '__main__':
    naam = input('Wat is uw naam?: ')
    groep = input('Wat is de groep?: ')
    print(maak_verwelkoming_klas(naam,groep))
