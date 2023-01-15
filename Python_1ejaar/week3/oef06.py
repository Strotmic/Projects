start = int(input('Geef een startwaarde op '))
stop = int(input('Geef een stopwaarde op '))

for i in range(start,stop):
    if i%7 ==0:
        if i% 5 ==0:
            pass
        else:
            print(i)