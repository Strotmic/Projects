import random

ran = random.randint(0,20)
count = 0
while True:
    getal = int(input('Raad een getal tussen 0 en 20: '))
    count+=1
    if getal ==ran:
        print(f'Proficiat je hebt het geraden in {count} keer')
        break
    elif getal < ran:
        print('groter')
    elif getal > ran:
        print('kleiner')
