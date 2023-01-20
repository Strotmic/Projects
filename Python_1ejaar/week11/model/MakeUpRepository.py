import json
from typing import List
from model.MakeUpProduct import MakeUpProduct
from model.ProductColor import ProductColor
import logging

class MakeUpRepository:
    # privaat klasse-attribuut
    __filename = "doc/makeupproducts.json"

    #static-methodes
    @staticmethod
    def __read_local_json_file(bestandsnaam):
        fo = open(bestandsnaam, encoding="utf8")
        response_json = fo.read()
        fo.close()
        return json.loads(response_json)        

    @staticmethod
    def load_products() -> List[MakeUpProduct]:
        resultaat = []      #hierin komen objecten van de klasse MakeUpProduct
        list_producten = MakeUpRepository.__read_local_json_file(MakeUpRepository.__filename)

        #list overlopen: de ingelezen list bestaat uit dictionaries
        for dict_product in list_producten:
            try:
                # haal alle info op: id, name, price, brand, productlink
                id = dict_product["id"]
                name = dict_product["name"]
                brand = dict_product["brand"]
                price = float(dict_product["price"])
                productlink = dict_product["product_link"]

                # maak een object aan van de klasse MakeUpProduct
                nieuw_product = MakeUpProduct(id, brand, name, price, productlink)
                

                #kleuren ook registreren
                #ophalen via de key --> opnieuw een list van dictionaries!!
                list_colors = dict_product["product_colors"]
                for dict_color in list_colors:
                    hexvalue = dict_color["hex_value"]
                    colorname = dict_color["colour_name"]
                    #object aanmaken van de klasse ProductColor
                    new_productcolor = ProductColor(colorname, hexvalue)
                    #toevoegen aan eerder aangemaakt make-up product
                    nieuw_product.add_productcolor(new_productcolor)

                #voeg toe aan de list
                resultaat.append(nieuw_product)
            except ValueError as ex:
                logging.error(f"Value-Error: {ex}")
            except Exception as ex:
                logging.error(f"Error: {ex}")
        return resultaat

    @staticmethod
    def search_in_products(listproducts: List[MakeUpProduct], searchpattern: str) -> List[MakeUpProduct]:
        results = []
        for product in listproducts:
            if searchpattern.lower() in product.name.lower():
                results.append(product)
        return results

    #ToDo: mooie extra oefening: geef de makeupproducts terug die een (deel van een) specifieke kleurnaam bevatten
    @staticmethod
    def search_in_products_with_color(listproducts: List[MakeUpProduct], search_colorname: str) -> List[MakeUpProduct]:
        results = []
        #vervolledig!
        return results  

