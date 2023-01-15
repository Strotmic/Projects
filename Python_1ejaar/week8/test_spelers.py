from model.Geboortedatum import Geboortedatum
from model.Speler import Speler

# def test_oef1():
#     Speler.naam_ploeg = "Rode duivels"

#     sp1 = Speler("Thibault", "Cortois", "keeper", 8, 0)
#     sp2 = Speler("Vincent", "Kompany", "aanvaller", 8, 3)
#     sp3 = Speler("Axel", "Witsel", "aanvaller")
#     team = [sp1, sp2, sp3]
#     print(team)

#     print("\nVincent scoort!")
#     sp2.maak_doelpunt()
#     print(sp2)

#     print("\nAxel scoort!")
#     sp3.maak_doelpunt()
#     print(sp3)

#     print(
#         f"Het doelpunten saldo van { Speler.naam_ploeg } is { Speler.get_doelpunten_saldo_ploeg()}")
#     pass


# test_oef1()


def test_spelers_oef3():
    sp1 = Speler("Thibault", "Cortous", "keeper",
                 8, 0, Geboortedatum(11, 5, 1992))
    sp2 = Speler("Vincent", "Kompany", "aanvaller",
                 8, 3, Geboortedatum(10, 4, 1986))
    sp3 = Speler("Axel", "Witsel", "aanvaller")

    print("\nDe geboortedata van de spelers zijn:")
    for item in [sp1, sp2, sp3]:
        print(f"{item} -> gebootedatum: {item.geboortedatum}")
    pass


test_spelers_oef3()
