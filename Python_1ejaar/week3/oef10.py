def geef_ticket_per_categorie(naam,totaal,producten):
    print(f'{producten} producten zitten in de categorie {naam}')
    print(f'totale kostprijs: {round(totaal,2)} totale prijs')
    print(f'gemiddelde prijs per product: {round((totaal/producten),2)} \n')

aantal = int(input('geef het aantal producten dat u went in te voeren: '))
producten = {'G':[0,0],'F':[0,0],'D':[0,0]}

for i in range(aantal):
    product = input('Wat is de categorie? [G:groente, F:Fruit, D:Drank]: ')
    prijs = float(input('Geef de prijs op: '))
    producten[product][0]+=1
    producten[product][1] +=prijs

geef_ticket_per_categorie('Groenten',producten['G'][1],producten['G'][0])
geef_ticket_per_categorie('Fruit',producten['F'][1],producten['F'][0])
geef_ticket_per_categorie('Groenten',producten['D'][1],producten['D'][0])

# for i in producten.keys():
#     som=0
#     print(f'{producten[i][0]} producten zitten in de categorie {i}')

#     for o in range(1,len(producten[i])): som+=producten[i][o]

#     print(f'totale kostprijs: {round(som,2)} totale prijs')

#     if len(producten[i])==1:
#         print(f'Gemiddelde prijs per product: 0.00')
#     else:
#         print(f'gemiddelde prijs per product: {round(som/(len(producten[i])-1),2)} \n')
