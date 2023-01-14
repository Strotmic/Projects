getal1 = int(input("Geef het minimum op:> "))
getal2 = int(input("Geef het maximum op:> "))

import random
def kies_5_getallen(x,y):
    l=[]
    if y-x <4:
        return 'Fout verschil is niet groter dan 5'
    while len(l)!=5:
        t = random.randint(x,y)
        if t not in l:
            l.append(t)
        else:
            pass
    return l


print(f"De vijf geselecteerde getallen hiertussen zijn: {kies_5_getallen(getal1, getal2)}")
