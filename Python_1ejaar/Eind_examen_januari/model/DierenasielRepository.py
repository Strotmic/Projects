import json
from model.Dierenasiel import Dierenasiel
from model.Kennel import Kennel
from model.Dier import Dier
from datetime import datetime


class DierenasielRepository:
    # __filename = "doc/dierenasiel_kortrijk.json"
    __filename = "doc/dierenasiel_brugge.json"

    @staticmethod
    def __read_local_json_file(bestandsnaam):
        fo = open(bestandsnaam, encoding="utf8")
        response_json = fo.read()
        fo.close()
        return json.loads(response_json)

    @staticmethod
    def inlezen_data_dierenasiel():
        dic = DierenasielRepository.__read_local_json_file(
            DierenasielRepository.__filename)
        try:
            asiel_naam = dic['dierenasiel']['naam']
            asiel_straat = dic['dierenasiel']['adres']['straat']
            asiel_stad = dic['dierenasiel']['adres']['stad']
            asiel_postcode = dic['dierenasiel']['adres']['postcode']
            asiel_telefoon = dic['dierenasiel']['telefoon']
            asiel_email = dic['dierenasiel']['email']
            asiel_vergunning = dic['dierenasiel']['vergunning']
            asiel = Dierenasiel(asiel_naam, asiel_straat, asiel_stad,
                                asiel_postcode, asiel_telefoon, asiel_email, asiel_vergunning)
        except ValueError as c:
            print(c)
        for ken in dic['dierenasiel']['kennels']:
            try:
                kennel_id = ken['kennel_id']
                kennel_type = ken['type']
                kennel_gekuist = ken['gekuist']
                kennel = Kennel(kennel_id, kennel_type, kennel_gekuist)
            except ValueError as c:
                print(c)

            for d in ken['dieren']:
                try:
                    dier_naam = d['naam']
                    dier_geboortedatum = datetime.strptime(d['geboortedatum'], '%Y-%m-%d')
                    dier_inschrijving = datetime.strptime(d['inschrijvingsdatum'], '%Y-%m-%d')
                    dier_ras = d['ras']
                    dier_geslacht = d['geslacht']
                    dier_gecast = d['gecastreerd']
                    dier = Dier(dier_naam,dier_geboortedatum,dier_inschrijving,dier_ras,dier_geslacht, dier_gecast)
                except ValueError as c:
                    print(c)
                kennel.voeg_dier_toe(dier)
            asiel.voeg_kennel_toe(kennel)

        return asiel

    @staticmethod
    def filter_op_ras(asiel,ras):
        ret =[]
        for i in asiel.kennels:
            for d in i.dieren:
                if d.ras.lower() == ras.lower():
                    ret.append(d)
        return ret

    def aantallen_per_ras(asiel):
        dic ={}

        for i in asiel.kennels:
            for d in i.dieren:
                if d.ras not in dic.keys():
                    dic[d.ras] = 1
                else:
                    dic[d.ras] +=1
        return dic