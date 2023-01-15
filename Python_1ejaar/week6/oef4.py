# ENKEL MCT!
# Gebruik bestand in doc/spelers.txt

# -	Functie ‘inlezen_spelers’ die het bronbestand correct inleest en de data in een datastructuur teruggeeft
# -	Functie ‘print_spelers’ die in staat is om alle spelers uit de gekozen datastructuur af te printen
# -	Functie ‘selecteer_random_elftal’ die in staat is om 11 verschillende spelers willekeurig te selecteren en terug te geven.
# -	Functie ‘opslaan_ploegopstelling’ die in staat is om een opstelling naar een tekstbestand  weg te schrijven.
import random
import re

def inlezen_spelers(doc):
    f = open(doc, 'r')
    return f
    f.close()

def print_spelers(doc):
    print( doc.read())

def selecteer_random_elftal(doc):
    l=[]
    p = doc.readlines()
    while len(l) != 11:
        i = random.randint(0,len(p)-1)
        l.append(p[i])
    for i in l:
        x = re.sub('\n','',i)
        l[l.index(i)] = x
    return l
        

x= inlezen_spelers('doc/spelers.txt')

print(selecteer_random_elftal(x))
