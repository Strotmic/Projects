from model.MakeUpProduct import MakeUpProduct
from model.MakeUpRepository import MakeUpRepository


list_products = MakeUpRepository.load_products()
list_products.sort()
print(f"Aantal ingelezen make-up producten: {len(list_products)}")

#voorbeeld: primer
zoekterm = input("Geef een deel van de naam op:> ")
results = MakeUpRepository.search_in_products(list_products, zoekterm)
print("Dit zijn de gevonden producten: ")
for product in results:
    print(product)
