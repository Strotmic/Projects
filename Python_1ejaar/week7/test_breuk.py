
from model.Breuk import Breuk

print("Breuk 1: ")
b1 = Breuk(3, 4)
print(b1)
print("Noemer wijzigen naar 6: ")
b1.noemer = 6
print(b1)
print("Breuk 1  laten vereenvoudigen: ")
b1.vereenvoudig()
print(b1)

print("\nBreuk 2 na verenvoudiging: ")
b2 = Breuk(4, 10)
print(b2)
print("Som van Breuk 1 en Breuk 2: ")
som = b1 + b2
print(som)