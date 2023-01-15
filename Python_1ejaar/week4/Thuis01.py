list_getallen1 = [4, 5, 6, 4]
list_getallen2 = [6, 5,4,28]
def zijn_totaal_verschillend(l,x):
    l=l.sort()
    x=x.sort()
    if l == x:
        return True
    else:
        return False

if __name__ == '__main__':
    print(zijn_totaal_verschillend(list_getallen1, list_getallen2))