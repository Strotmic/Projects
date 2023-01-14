from model.Presentator import Presentator
from model.Tvprogramma import Tvprogramma
from model.Zender import Zender


presentator1 = Presentator("Laura", "Tesoro")
presentator2 = Presentator("Nathalie", "Meskens")


programma1 = Tvprogramma("Belgium got talent", presentator1)
programma2 = Tvprogramma("Beste kijkers", presentator2)
programma2.is_actief = False

# Verkort
programma3 = Tvprogramma("The Late Late Show", Presentator("James", "Corden"))


zender1 = Zender("VTM", "NL")
zender2 = Zender("FOX", "ENG")
zender3 = Zender("TV China", "Chinees")

zender1.voeg_programma_toe(programma1)
zender1.voeg_programma_toe(programma2)
zender2.voeg_programma_toe(programma3)
zender2.voeg_programma_toe("dit zal niet lukken")

print("*** info zenders ***")
print(zender1)
print(zender2)
print(zender3)
print(f"**** volgende programma's zijn afgelopen van {zender1.naam}  ***")
print(zender1.zoek_afgelopen())
print(
    f"**** volgend programma wordt willekeurig gekozen van {zender1.naam} ***")
print(zender1.selecteer_willekeurig_programma())
print(
    f"Aantal verschillende zenders aangemaakt {Zender.geef_aantal_aangemaakte_zenders()}")
