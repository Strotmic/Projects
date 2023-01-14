getallen = [12, 45, 465, 78, 1, 23, 89]
lege_lijst_getallen = []

def gemiddelde_in_list(l):
    if len(l) == 0:
        return ' oh dear'
    else:
        return (sum(l)/len(l))

if __name__ == '__main__':
    print(gemiddelde_in_list(getallen))
    print(gemiddelde_in_list(lege_lijst_getallen))
