from model.Presentator import Presentator
from model.Tvprogramma import Tvprogramma


presentator1 = Presentator("Laura", "Tesoro")
presentator2 = Presentator("Nathalie", "Meskens")
programma1 = Tvprogramma("Belgium got talent", presentator1)
programma2 = Tvprogramma("Beste kijkers", presentator2)
programma2.is_actief = False

# Verkort
programma3 = Tvprogramma("The Late Late Show", Presentator("James", "Corden"))

# geeft een fout
programma4 = Tvprogramma("The Simpsons", "Homer Simpson")
print("*** toon info ***")
print(programma2)
print(programma3)
print(programma4)
print(f"{programma2} is momenteel actief: {programma2.is_actief}")
programma2.is_actief = True
print(f"{programma2} is momenteel actief: {programma2.is_actief}")
programma2.is_actief = "blablablabla"
print(f"{programma2} is momenteel actief: {programma2.is_actief}")
