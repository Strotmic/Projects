from model.Personenwagen import Personenwagen
from model.Vrachtwagen import Vrachtwagen

voertuig1 = Personenwagen(100, "Audi", 2010, 3000, 5)
voertuig2 = Personenwagen(101, "Volkswagen", 2016, 0, 5)
voertuig3 = Vrachtwagen(102, "DAF", 2009, 3000, 5000)

verhuurlist = [voertuig1, voertuig2, voertuig3]
print("*** Dit zijn de beschikbare voertuigen ****")
for item in verhuurlist:
    print(item)

print("*** Geef de nieuwe bestemming van de voertuigen ****")
for item in verhuurlist:
    temp_reisbestemming = input(f"Voor {item} > ")
    item.reisbestemming = temp_reisbestemming

print("*** Er stappen 3 personen in de Volkswagen ****")
verhuurlist[1].aantal_personen = 3
print("*** De vrachtwagen wordt geladen ****")
try:
    temp_vracht = float(input(f"Hoeveel vracht neemt deze vrachtwagen mee? (max: {verhuurlist[2].max_laadvermogen}) > "))
    verhuurlist[2].vracht = temp_vracht
except Exception as ex:
    print(f"Foutje: {ex}")

print("*** toon details per rental car ****")
for item in verhuurlist:
    print(item.geef_detail_info())

print("*** De vrachtwagen wordt geladen ****")
try:
    temp_vracht = float(input(f"Hoeveel vracht neemt deze vrachtwagen mee? (max: {verhuurlist[2].max_laadvermogen}) > "))
    verhuurlist[2].vracht = temp_vracht
except Exception as ex:
    print(f"Foutje: {ex}")