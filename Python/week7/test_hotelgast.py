from model.Hotelgast import Hotelgast

gast1 = Hotelgast("Walcarius", 'Stijn', -100, True)
gast2 = Hotelgast("Roobrouck", "Dieter", 30, False)

print("*** Volgende gasten verblijven bij ons: ")
print(gast1.voornaam)
print(gast1)
print(gast2)
print("**** checkt uit met fout")
gast1.ingecheckt = '26'
print(gast1)