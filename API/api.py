from flask import Blueprint, jsonify, make_response, request
from banco import Banco

bp_api = Blueprint('api',__name__,url_prefix="/jogos/api/v1/lista")
banco = Banco()


@bp_api.route("/",methods=['GET'])
@bp_api.route("/<int:id>",methods=['GET'])
def get_games(id = None):
    lista = banco.listJogos()
    if lista != False:
      if id != None:
         lista = banco.getJogo(id)
         return jsonify({'lista':lista})
      else:
         return jsonify({'lista':lista})
    else:
      return make_response(jsonify({"error":"Not existe DADO carai"}),404)     


@bp_api.route("/add/",methods=['POST'])
def add_games():
   if request.json:
    banco.saveJogo(request.json[0])     
   return make_response(jsonify({"msg":"Dados Inseridos com Sucesso"}),200)     

@bp_api.route("/alter/<int:id>",methods=['PUT'])
def put_games(id = None):
    if request.json and id != None:
        banco.updateJogo(id, request.json[0])     
    return make_response(jsonify({"msg":"Dados ALTERADOS com Sucesso"}),200)     




@bp_api.route("/del/<int:id>",methods=['DELETE'])
def del_games(id  = None) :
    if request.json  and id != None:
      banco.deleteJogo(id)     
    return make_response(jsonify({"msg":"Dado {} DELETADO  com Sucesso".format(id)}),200)     

