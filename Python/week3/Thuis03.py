from oef11 import is_schrikkeljaar

start = int(input('Geef een startjaar op: '))
stop = int(input('Geef een stopjaar op: '))
for i in range(start,stop+1):
    if is_schrikkeljaar(i) == True: print(i)
