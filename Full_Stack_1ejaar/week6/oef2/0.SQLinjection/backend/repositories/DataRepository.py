from .Database import Database


class DataRepository:
    @staticmethod
    def json_or_formdata(request):
        if request.content_type == 'application/json':
            gegevens = request.get_json()
        else:
            gegevens = request.form.to_dict()
        return gegevens

    #########  Bestemmingen  #########
    @staticmethod
    def read_bestemming_ok(BestemmingID):
        # *** Correcte techniek ***
        sql = "SELECT * FROM tblBestemming WHERE BestemmingID = %s"
        params = [BestemmingID]
        data = Database.get_rows(sql, params)
        return data

    @staticmethod
    def read_bestemming_nok(BestemmingID):
        # 💣 dit moet mis gaan!
        sql = f"SELECT * FROM tblBestemming WHERE BestemmingID = {BestemmingID}"
        data = Database.get_rows(sql)
        return data
