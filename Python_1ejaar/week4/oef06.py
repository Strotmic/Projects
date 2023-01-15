woord = input("Geef een woord op? > ")
list = ['a','e','y','u','i','o']
woord = [*woord]

klinkers = []
medeklinkers =[]
for i in woord:
    if i in list:
        klinkers.append(i)
    else:
        medeklinkers.append(i)

print(f'De gevonden klinkers zijn {klinkers} \nen de medeklnkers zijn {medeklinkers}')