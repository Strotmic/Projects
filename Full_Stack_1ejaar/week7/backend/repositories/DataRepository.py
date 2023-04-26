from .Database import Database


class DataRepository:
    @staticmethod
    def json_or_formdata(request):
        if request.content_type == 'application/json':
            gegevens = request.get_json()
        else:
            gegevens = request.form.to_dict()
        return gegevens

    #########  treinen  #########
    @staticmethod
    def read_treinen():
        sql = 'select * from treinen'
        return Database.get_rows(sql)

    @staticmethod
    def read_trein(treinid):
        sql = 'select * from treinen where idtrein=%s'
        params = [treinid]
        return Database.get_one_row(sql, params)

    @staticmethod
    def create_trein(vertrek, bestemmingID, spoor, vertragin, afgeschaft):
        sql = 'insert into treinen(vertrek,bestemmingid,spoor,vertraging,afgeschaft) values(%s,%s,%s,%s,%s)'
        params = [vertrek, bestemmingID, spoor, vertragin, afgeschaft]
        return Database.execute_sql(sql, params)
    
    @staticmethod
    def update_trein(vertrek, bestemmingID, spoor, vertragin, afgeschaft, id):
        sql = 'update treinen set vertrek=%s, bestemmingid=%s, spoor=%s, vertraging=%s, afgeschaft=%s where idtrein=%s'
        params = [vertrek, bestemmingID, spoor, vertragin, afgeschaft,id]
        return Database.execute_sql(sql, params)

    @staticmethod
    def delete_trein(id):
        sql='delete from treinen where idtrein=%s'
        params=[id]
        return Database.execute_sql(sql, params)
    
    @staticmethod
    def update_trein_vertraging(idtrein, vertraging):
        sql ='UPDATE treinen SET vertraging = %s WHERE idtrein = %s'
        params=[vertraging,idtrein]
        return Database.execute_sql(sql,params)
    #########  bestemmingen  #########

    @staticmethod
    def read_bestemmingen():
        sql = 'select * from bestemmingen'
        return Database.get_rows(sql)

    @staticmethod
    def read_treinen_met_bestemming(bestemmingid):
        sql = 'SELECT * FROM treinen t INNER JOIN bestemmingen b ON t.bestemmingID = b.idbestemming WHERE idbestemming = %s'
        params = [bestemmingid]
        return Database.get_rows(sql, params)
