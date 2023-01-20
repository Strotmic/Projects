import random
from model.Auto import Auto

autos = []
autos.append(Auto("Volkswagen", "passat", "donkergrijs", "diesel"))
autos.append(Auto("Opel", "astra", "groen", "benzine"))
autos.append(Auto("Seat", "ibiza", "blauw", "diesel"))

for auto in autos:
    print(f"Auto {auto} heeft op de kmteller {auto.kmstand}")
print("\nOp het einde van de dag: ")
for auto in autos:
    auto.rijden(random.randint(10, 300))
    print(
        f"\tAuto {auto} heeft op de kmteller {auto.kmstand} en \
doet {auto.maak_lawaai()}")
