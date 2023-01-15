maanden = ["januari", "februari", "maart", "april", "mei", "juni", "juli", "augustus", "september", "oktober","november", "decemeber"]
getallen = [100, 200, 300, 400]

import random
def kies_element(l):
    return f'het gekozen item is {l[random.randint(0,len(l)-1)]}'

if __name__ =='__main__':
    print(kies_element(maanden))
    print(kies_element(getallen))
