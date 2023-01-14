from model.Bier import Bier
from model.BierRepository import BierRepository


def print_bieren(lijst_bieren):
    for bier in lijst_bieren:
        print(f"{bier} -> alcoholpercentage: {bier.alcoholpercentage}")


def test_bieren_a():
    # opgave a
    lijst_bieren = BierRepository.inlezen_bieren()
    print(f"Aantal correct ingelezen bieren zijn: {len(lijst_bieren)}")
    print(f"Inhoud van de lijst met bieren: {lijst_bieren}")


# test_bieren_a()


def test_bieren_b():
    # opgave b
    lijst_bieren = BierRepository.inlezen_bieren()
    lijst_bieren.sort()
    print_bieren(lijst_bieren)


# test_bieren_b()


def test_bieren_c():
    # opgave c
    lijst_bieren = BierRepository.inlezen_bieren()
    lijst_bieren.sort()
    deel_brouwerij = input("\nGeef (een deel van) de brouwerijnaam op: ")
    print("Gevonden bieren zijn: ")
    resultaat = BierRepository.zoek_bieren_uit_brouwerij(
        lijst_bieren, deel_brouwerij)
    print_bieren(resultaat)

test_bieren_c()
