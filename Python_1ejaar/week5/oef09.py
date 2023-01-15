list_personeel = ["Stijn", "Gilles", "Dieter", "Christophe"]
# random snelheid
# printen snelheidsmeting
# opvragen max_snelheid
# filteren van overtredingen

import random

def registreer_snelheidsmeting(lid):
    dic={}
    for i in lid:
        dic[i] = random.randint(30,70)
    return dic

def print_snelheden_personen(straatnaam, dic):
    print(f'{straatnaam}')
    for i in dic.keys():
        print(f'{i:30s}{dic[i]}')

def print_boetes(dic,snelheid):
    print('Boete:')
    for i in dic.keys():
        if dic[i]>snelheid:
            print(f'{i :30s} boete: {(dic[i]-snelheid)*10}')


snelheid = int(input('geef de maximum toegelaten snelheid op: '))

dic = registreer_snelheidsmeting(list_personeel)
print_snelheden_personen('Test', dic)
print_boetes(dic,snelheid)


