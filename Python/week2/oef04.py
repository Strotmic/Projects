leeftijd = int(input('Geef de leeftijd van uw hond?: '))

if leeftijd <= 0:
    print('Fout geef een andere leeftijd op')

if leeftijd ==1:
    print('de leeftijd komt overeen met 14 mensenjaren')
elif leeftijd ==2:
    print('de leeftijd komt overeen met 22 mensenjaren')
else: 
    print(f'de leeftijd komt overeen met {22+((leeftijd-2)*5)} mensenjaren')