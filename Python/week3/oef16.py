import random
from string import ascii_letters

def genereer_paswoord_bis(start,stop):
    lengte= random.randint(start,stop)
    dic = [*ascii_letters]
    ww=''
    for i in range(lengte):
        ww+= random.choice(dic)
    return ww

start = int(input('Geef een min waarde op: '))
stop = int(input('Geef een max waarde op: '))
ww = genereer_paswoord_bis(start,stop)
print(f'De lengte is {len(ww)}')
print(ww)