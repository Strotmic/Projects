# MCT/ MIT
# Schrijf een tekst weg naar temp.txt
import os


def lees_bestand_in(bestandsnaam):
    f = open(bestandsnaam) #geeft file object terug
    l = f.read().splitlines()
    lr = 1
    for x in l:
        lr += 1
        print(f"- regel {lr}: {x}")
    f.close()
 
 
def schrijf_input_naar_bestand(bestandsnaam):
    f = open(bestandsnaam, "w")
    x = str(input("Geef een nieuwe regel op: "))
    while x!= "":
        f.write(x + "\n")
        x = str(input("Geef een nieuwe regel op: "))
    f.close()



if os.path.exists("doc/temp.txt") == True:
    lees_bestand_in("doc/temp.txt")
else:
    schrijf_input_naar_bestand("doc/temp.txt")