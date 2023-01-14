# input( "Geef de naam van een vriend op, of sluit af met een leeg veld: ")
l=[]

while True:
    vriend = input('Geef een vriend op of sluit af met een leeg veld: ')
    if vriend == '':
        break
    else:
        l.append(vriend)
print(l)