from typing import List
from model.Personenwagen import Personenwagen
import json


class PersonenwagenRepository:
    __filename = "doc/auto.json"

    @staticmethod
    def __read_local_json_file():
        fo = open(PersonenwagenRepository.__filename, encoding="utf8")
        response_json = fo.read()
        fo.close()
        return json.loads(response_json)

    @staticmethod
    def inlezen_personenwagens():
        ret =[]
        dic = PersonenwagenRepository.__read_local_json_file()
        for i in dic:
            ret.append(Personenwagen(i['Auto-id'],i['Merk'],i['Bouwjaar'],i['Km-stand'],i['Max-plaatsen']))
        return ret
    
    @staticmethod
    def zoek_wagen(l,id):
        for i in l:
            if i.id == id:
                return i