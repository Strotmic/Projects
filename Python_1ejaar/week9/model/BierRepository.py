from .Bier import Bier 
import json
class BierRepository:
    __filename = "doc/bieren.json"
    @staticmethod
    def inlezen_bieren():
        bieren = []
        list_bieren = BierRepository.__inlezen_local_json_file(BierRepository.__filename) 
        for dict_bier in list_bieren:
            try:
                obj = Bier(dict_bier['Naam'], dict_bier['Brouwerij'],dict_bier['alcohol'],dict_bier['Kleur'])
                bieren.append(obj)
            except ValueError as c:
                print(c)

        return bieren

    @staticmethod
    def __inlezen_local_json_file(bestandsnaam):
        fo = open(bestandsnaam) 
        response_json = fo.read() 
        fo.close()
        return json.loads(response_json)
        
    @staticmethod
    def zoek_bieren_uit_brouwerij(lijst, naam):
        ret =[]
        for i in lijst:
            if i.brouwerij.lower() == naam:
                ret.append(i)
        return ret