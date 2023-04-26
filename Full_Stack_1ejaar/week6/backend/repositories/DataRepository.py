from .Database import Database


class DataRepository:
    @staticmethod
    def json_or_formdata(request):
        if request.content_type == 'application/json':
            gegevens = request.get_json()
        else:
            gegevens = request.form.to_dict()
        return gegevens

  #########  Klanten  #########

    @staticmethod
    def read_klanten():
        sql = "SELECT * FROM tblklant"
        data = Database.get_rows(sql)
        return data

  #########  Bestemmingen  #########
