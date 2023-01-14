list = ['a','e','y','u','i','o']
woord = input('Geef een woord op: ')

for i in woord:
    if i in list:
        woord = woord.replace(i,'*')
print(woord)

        
