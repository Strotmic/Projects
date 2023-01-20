from model.Dier import Dier
from model.Kennel import Kennel
from model.Dierenasiel import Dierenasiel
from datetime import datetime

def maak_dieren():
    print("\n*** Test 1 ***")
    print('*** 1a) aanmaken dier')
    hond1 = Dier("Max", datetime(2019,1,31), datetime(2023,1,10),"Golden Retriever","m", True)
    print(hond1)

    print('*** 1b) tweede & derde dier aanmaken en vergelijken')
    hond2 = Dier("Lucy", datetime(2020,10,5), datetime(2022,11,10),"Bulldog","v", False)
    hond3 = Dier("Lucy", datetime(2020,10,5), datetime(2022,11,10),"Bulldog","v", False)
    if hond1 ==  hond2:
        print("hond1 en hond2 zijn gelijk")
    else:
        print("hond1 en hond2 zijn NIET gelijk")
    if hond2 ==  hond3:
        print("hond2 en hond3 zijn gelijk")
    else:
        print("hond2 en hond3 zijn NIET gelijk")

    print("** 1c) Sorten en printen van een lijst")
    mijn_dieren = [hond1, hond2]
    print(f"Niet gesorteerd: {mijn_dieren}")
    mijn_dieren.sort()
    print(f"Gesorteerd op geboortedatum (jongste eerst): {mijn_dieren}")

    print("** 1d) geslacht wordt altijd in hoofdletters afgeprint")
    print(f"Geslacht van {hond1.naam}: {hond1.geslacht}")


def maak_kennel():
    print("\n*** Test 2 ***")
    print('*** 2a) aanmaken kennel')   
    honden_kennel = Kennel("1SX", "honden")
    print(honden_kennel)
    print(f"Kennel gekuist? {honden_kennel.is_gekuist}")

    print('*** 2b) Honden toevoegen aan kennel')  
    hond1 = Dier("Max", datetime(2019,1,31), datetime(2023,1,10),"Golden Retriever","m", True)
    hond2 = Dier("Lucy", datetime(2020,10,5), datetime(2022,11,10),"Bulldog","v", False)
    honden_kennel.voeg_dier_toe(hond1)
    honden_kennel.voeg_dier_toe(hond2)
    print(f"Aantal dieren aanwezig in kennel: {honden_kennel.aantal_dieren}")
    print(f"Dieren aanwezig in kennel: {honden_kennel.dieren}")
    
    print("*** 2c) Is Lucy in de kennel aanwezig?")
    lucky_dog = honden_kennel.vind_dier_via_naam("Lucy")
    print(f"Gevonden: {lucky_dog}")

    print("*** 2d) Sorteren van kennels volgens aantal dieren?")
    katten_kennel = Kennel("1AX", "cats")
    kat1 = Dier("Krispy", datetime(2021,6,5), datetime(2022,9,25),"Siamese","v", True)
    katten_kennel.voeg_dier_toe(kat1)    
    mijn_kennels = [honden_kennel, katten_kennel]
    print(f"Niet gesorteerd: {mijn_kennels}")
    mijn_kennels.sort()
    print(f"Gesorteerd op aantal dieren in kennel: {mijn_kennels}")

    
def maak_dierenasiel():
    print("\n*** Test 3 ***")
    print('*** 3a) aanmaken asiel')
    mijn_asielcentrum = Dierenasiel("Asielcentrum MCT","Graaf Karel de goedelaan 5", "Kortrijk", "8500","056241244", "info@howest.be", True)
    print(mijn_asielcentrum)
    print(f"Contact: {mijn_asielcentrum.straat} {mijn_asielcentrum.stad}, tel: {mijn_asielcentrum.telefoonnummer}, e-mail: {mijn_asielcentrum.emailadres}")
    print(f"Is vergund? {mijn_asielcentrum.is_vergund}")

    print('*** 3b) toevoegen van kennels met dieren')
    honden_kennel = Kennel("1SX", "honden")
    hond1 = Dier("Max", datetime(2019,1,31), datetime(2023,1,10),"Golden Retriever","m", True)
    hond2 = Dier("Lucy", datetime(2020,10,5), datetime(2022,11,10),"Bulldog","v", False)
    honden_kennel.voeg_dier_toe(hond1)
    honden_kennel.voeg_dier_toe(hond2)
    mijn_asielcentrum.voeg_kennel_toe(honden_kennel)

    katten_kennel = Kennel("1AX", "katten")
    kat1 = Dier("Krispy", datetime(2021,6,5), datetime(2022,9,25),"Siamese","v", True)
    katten_kennel.voeg_dier_toe(kat1)    
    mijn_asielcentrum.voeg_kennel_toe(katten_kennel)
    print(f"Kennels: {mijn_asielcentrum.kennels}")
    print(f"Totaal aantal dieren aanwezig in asiel: {mijn_asielcentrum.aantal_dieren}")

    
def maak_kennel_met_fouten():
    print("\n*** Test 4 - Foutieve invoer bij een kennel ***")
    try:
        hond1 = Dier("Max", datetime(2019,1,31), datetime(2023,1,10),"Golden Retriever","x", True)
        print(hond1)
    except Exception as ex:
        print(f"FOUTJE: {ex}")

    try:
        katten_kennel = Kennel("1AX", "cats")
        katten_kennel.voeg_dier_toe("doggie")
    except Exception as ex:
        print(f"FOUTJE: {ex}")


# maak_dieren()
# maak_kennel()
# maak_dierenasiel()
maak_kennel_met_fouten()