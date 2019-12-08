import dataset

class Banco:
    def listJogos(self):
        with dataset.connect("sqlite:///apijogos.db") as db:
                jogos = db["jogos"].all()
                if db['jogos'].count() > 0:
                    listaJogos = [dict(id=data['id'],nome=data['nome'], platform=data['platform'],Price=data['Price']) for data in jogos]
                    return listaJogos
                else:
                    return False

    def saveJogo(self,data):
        with dataset.connect("sqlite:///apijogos.db") as db:
            return db['jogos'].insert(dict(id=data['id'],
                nome=data['nome'], 
                platform=data['platform'],
                Price=data['Price']))

    def getJogo(self, id):
        with dataset.connect("sqlite:///apijogos.db") as db:
            jogo = db['jogos'].find_one(id=id)
            if jogo:
                return jogo
            else:
                return False
    def updateJogo(self, id, data):
        with dataset.connect("sqlite:///apijogos.db") as db:
            return db['jogos'].update(dict(id=id,nome=data['nome'],platform=data['platform'],Price=data['Price']),['id'])

    def deleteJogo(self, id):
        with dataset.connect("sqlite:///apijogos.db") as db:
            return db['jogos'].delete(id=id)

