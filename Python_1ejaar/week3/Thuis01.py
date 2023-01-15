woord = input('Geef een woord op: ')
list = ['a','e','y','u','i','o']
klinkers =0
medeklinkers = len(woord)
for i in (woord):
    if i in list:
        klinkers+=1
print(f'Aantal klinkers {klinkers}')
print(f'Het aantal medeklinkers {medeklinkers-klinkers}')
