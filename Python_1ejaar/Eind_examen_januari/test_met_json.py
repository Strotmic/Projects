from model.Dierenasiel import Dierenasiel
from model.DierenasielRepository import DierenasielRepository

print("****1) inlezen data dierenasiel ****")
mijn_asiel = DierenasielRepository.inlezen_data_dierenasiel()
print(mijn_asiel)
print(f"Aantal aanwezige dieren: {mijn_asiel.aantal_dieren}")
for kennel in mijn_asiel.kennels:
    print(f"{kennel} -> Gekuist? {kennel.is_gekuist}")
    print(f"\tDe dieren zijn: {kennel.dieren}")

print("\n****2) Rassen in het dierenasiel ****")
print(f"Zoeken naar Golden Retriever?")
print(DierenasielRepository.filter_op_ras(mijn_asiel,"golden retriever"))

print("\n****3) Aantallen per ras in dierenasiel ****")
print(f"Aantallen per ras in dierenasiel:")
for ras, aantal in DierenasielRepository.aantallen_per_ras(mijn_asiel).items():
    print(f"- Ras {ras} -> {aantal}")

