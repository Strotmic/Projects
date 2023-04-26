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

    @staticmethod
    def read_klant(id):
        sql = "select * from tblklant where KlantID=%s"
        params = [id]
        return Database.get_one_row(sql, params)

    @staticmethod
    def create_klant(naam,voornaam,straat,nr,postcode,gemeente):
        sql = "insert into tblklant(FNaam, VNaam, Straat, Nummer, Postcode, Gemeente) values(%s,%s,%s,%s,%s,%s)"
        params = [naam, voornaam, straat, nr, postcode, gemeente]
        return Database.execute_sql(sql,params)
    
    @staticmethod
    def update_klant(naam, voornaam, straat, nr, postcode, gemeente, id):
        sql = 'update tblklant set FNaam=%s, VNaam=%s,Straat=%s,Nummer=%s,Postcode=%s,Gemeente=%s where klantid=%s'
        params = [naam, voornaam, straat, nr, postcode, gemeente, id]
        return Database.execute_sql(sql,params)

    @staticmethod
    def delete_klant(id):
        sql = 'delete from tblklant where klantid=%s'
        params=[id]
        return Database.execute_sql(sql,params)
  #########  Bestemmingen  #########
