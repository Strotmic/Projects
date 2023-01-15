from model.Bier import Bier


def test1():
    bier = Bier("NMCT-Blond", "Howest", 25.0, "blond")
    print(bier)
    # geef een blanco naam op, via de input
    nieuwe_naam = input("Geef een nieuwe biernaam op:> ")
    bier.naam = nieuwe_naam
    print(bier)


test1()

def test2():
    biernaam = input("Geef de biernaam op:> ")
    brouwerijnaam = input("Geef de brouwerij op:> ")
    kleur = input("Geef de kleur op:> ")
    alcoholpercentage = float(input("Geef het alcoholpercentage op:> "))
    print("Bier aanmaken...")
    bier = Bier(biernaam, brouwerijnaam, alcoholpercentage, kleur)
    print(bier)


test2()
