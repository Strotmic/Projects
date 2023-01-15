list_getallen1 = [4, 5, 6, 4]
list_getallen2 = [89, 78, 4]

def zijn_totaal_verschillend(l,x):
    if len(set(l + x)) == len(l + x):
        return 'beide lijsten zijn uniek'
    else:
        return 'Er zit minstens 1 gemeenschappelijke waarde in list1 en list2'

if __name__ == '__main__':
    print(zijn_totaal_verschillend(list_getallen1, list_getallen2))