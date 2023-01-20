# Vervolledig de functie geef_provincie die voor een doorgegeven postcode (parameter) de juiste provincienaam teruggeeft. 
# We beperken ons tot de provincies uit Vlaanderen.  
# Er geldt dat: 
# • West-Vlaanderen:   postcodes tussen 8000-8999 
# • Oost-Vlaanderen:   postcodes tussen 9000-9999 
# • Antwerpen:     postcodes tussen 2000-2999 
# • Limburg:     postcodes tussen 3500-3999 
# • Vlaams-Brabant:    postcodes tussen 1500-1999 en 3000-3499 

# Hier hebben we 2 opties, of we werken met if structuren  (de lange manier).
#Of we werken met een dictionary die de postcodes bijhoud (de kortere manier)

# Manier 1 is met if en elifs werken. In dit geval is dit minder complex dan onderstaande manier (met dictionary).
# Maar deze manier is moeilijker en langer eens er meer provincies bijkomen.
def geef_provincie(gemeente: int) -> str:
    if gemeente >=8000 and gemeente <= 8999: # We checken of de waarde tussen 8000 en 8999 ligt
        return(f'West-Vlaanderen')

    elif gemeente >=9000 and gemeente <= 9999:
        return(f'Oost-Vlaanderen')

    elif gemeente >=2000 and gemeente <= 2999:
        return(f'Antwerpen')

    elif gemeente >=1500 and gemeente <= 1999 or gemeente >=3000 and gemeente <=3499:
        return(f'Vlaams-Brabant')
    elif gemeente >=3500 and gemeente <= 3999:
        return(f'Limburg')
    else:
        return(f'geen van de bovenstaande')


#Manier 2 om dit op te lossen met een Dictionary en lists (dit is een manier die meer toegankelijk is voor eventuele uitbreidingen later)
# Nu gaan we de values van de dictionary doorlopen (wat de lijsten zijn)
def geef_provincie2(gemeente: int) -> str:
    #In onderstaande dictionary geven we aan de naam van de provincie een lijst mee met de begin en eindwaarde van de postcodes 
    postcodes = {'West-Vlaanderen':[8000,8999],'Oost-Vlaanderen':[9000,9999],'Antwerpen':[2000,2999],'Limburg':[3500,3999],'Vlaams-Brabant':[1500,1999,3000,3499]}
    for prov, codes in postcodes.items():

        for leng in range(0,len(codes),2): #Hier doorlopen we de list value per stapgrootte 2, dit doen we want iedere startwaarde heeft ook een stopwaarde (dus gegroepeerd per 2)

            if gemeente >= codes[leng] and gemeente <= codes[leng+1]: # als de code tussen de start en de eind waarde ligt dan weten we dat de huidige prov de provincie is

                return(f'{prov}')
    return f'Geen overeenkomstige provincie'


# deze if zorgt ervoor dat deze code niet word uitgevoerd als we deze methode later importeren.
if __name__ == '__main__':
    gemeente = int(input('Geef een postcode op? > ')) # We casten dit naar een int want de postcode is een natuurlijk getal
    print(f'De provincie van postcode {gemeente} is {geef_provincie(gemeente)} ')

