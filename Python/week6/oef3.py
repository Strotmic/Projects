# MCT/ MIT
# Voeg tekst toe aan temp.txt indien deze bestaat

import os

def lees_bestand_in(bestandsnaam):
    f = open(bestandsnaam, 'a') #geeft file object terug
    x = str(input("Geef een nieuwe regel op: "))
    while x!= "":
        f.write(x + "\n")
        x = str(input("Geef een nieuwe regel op: "))
    f.close()
 
 
def schrijf_input_naar_bestand(bestandsnaam):
    f = open(bestandsnaam, "a")
    x = str(input("Geef een nieuwe regel op: "))
    while x!= "":
        f.write(x + "\n")
        x = str(input("Geef een nieuwe regel op: "))
    f.close()



if os.path.exists("doc/temp.txt") == True:
    lees_bestand_in("doc/temp.txt")
else:
    schrijf_input_naar_bestand("doc/temp.txt")
