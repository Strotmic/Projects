import json
from typing import List
from model.Ouder import Ouder
from model.Student import Student
import random
class OuderRepository:

    __filename = "doc/ouders.json"

    @staticmethod
    def __read_local_json_file():
        fo = open(OuderRepository.__filename, encoding="utf8")
        response_json = fo.read()
        fo.close()
        return json.loads(response_json)

    @staticmethod
    def inlezen_ouders_met_studenten():
        ret =[]
        t= OuderRepository.__read_local_json_file()
        for i in t:
            temp = Ouder(i['Naam'],i['Voornaam'],i['Geboortejaar'])
            for j in i['Studenten']:
                temp.voeg_student_toe(Student(j['Naam'],j['Voornaam'],random.randint(1,1000),j['Opleiding'],j['Geboortejaar']))
            ret.append(temp)
            
        return ret
    
    @staticmethod
    def filter_ouders_met_studenten_uit_opleiding(l,op):
        ret = []
        for i in l:
            print(i)
            for j in i.studenten:
                if j.opleiding == op:
                    ret.append(i)
        return ret

