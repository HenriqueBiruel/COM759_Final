from flask import json, request, jsonify
import flask
from bson import json_util
from app import app
from app import db
from bson.objectid import ObjectId

@app.route('/')
@app.route('/index')
def index():
    return flask.jsonify(json.loads(json_util.dumps(db.midias.find({}).sort("_id", 1))))

@app.route('/create', methods=['POST'])
def create():
    json_data = request.json
    if json_data is not None:
        db.midias.insert_one(json_data)
        return jsonify(mensagem='Mídia criada com sucesso!')
    else:
        return jsonify(mensagem='Erro ao criar mídia.')

@app.route("/getid/<string:midiaId>")
def getid(midiaId):
    midia = db.midias.find_one({"_id": ObjectId(midiaId)})
    return flask.jsonify(json.loads(json_util.dumps(midia)))

@app.route("/delete/<string:midiaId>")
def delete(midiaId):
    result = db.midias.delete_one({"_id": ObjectId(midiaId)})
    if(result.deleted_count > 0):
        return jsonify(mensagem='Mídia removida com sucesso!')
    else:
        return jsonify(mensagem='Erro ao remover mídia.')

@app.route('/update', methods=['POST'])
def update():
    json_data = request.json
    if json_data is not None and db.midias.find_one({"_id": ObjectId(json_data["id"])}) is not None:
        db.midias.update_one(
            {'_id': ObjectId(json_data["id"])},
            {"$set": {
                'titulo': json_data["titulo"],
                'tipo': json_data["tipo"],
                'genero': json_data["genero"],
                'ano': json_data["ano"],
                'descricao': json_data["descricao"],
                'avaliacao': json_data["avaliacao"]
            }}
        )
        return jsonify(mensagem='Mídia atualizada com sucesso!')
    else:
        return jsonify(mensagem='Erro ao atualizar mídia.')
