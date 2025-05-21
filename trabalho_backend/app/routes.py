from flask import json, request, jsonify
import flask
from bson import json_util
from app import app
from app import db
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import requests
import os
from dotenv import load_dotenv

load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")


# Rotas para mídias
@app.route('/')
@app.route('/list')
def getlist():
    return flask.jsonify(json.loads(json_util.dumps(db.midias.find({}).sort("_id", 1))))

@app.route('/create', methods=['POST'])
def create():
    json_data = request.json
    if json_data is not None:
        if not json_data.get("username"):
            return jsonify(mensagem='Campo "username" obrigatório para vincular a mídia ao usuário.'), 400

        db.midias.insert_one(json_data)
        return jsonify(mensagem='Mídia criada com sucesso!')
    else:
        return jsonify(mensagem='Erro ao criar mídia.')

@app.route('/list/<string:username>')
def getlist_by_user(username):
    """Lista mídias apenas do usuário especificado"""
    midias = db.midias.find({"username": username})
    return flask.jsonify(json.loads(json_util.dumps(midias)))



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

# Rotas para usuários
@app.route('/cadastro', methods=['POST'])
def cadastro_user():
    data = request.get_json()
    if not data.get('username') or not data.get('password') or not data.get('email'):
        return jsonify({'mensagem': 'Usuário, senha e email são obrigatórios!'}), 400

    # Verifica se o usuário já existe
    if db.usuario.find_one({'username': data['username']}):  # Usando a coleção 'usuario'
        return jsonify({'mensagem': 'Usuário já existe!'}), 400

    # Cria o usuário com senha criptografada
    hashed_password = generate_password_hash(data['password'])
    db.usuario.insert_one({
        'username': data['username'],
        'password': hashed_password,
        'email': data['email']
    })

    return jsonify({'mensagem': 'Usuário cadastrado com sucesso!'}), 201

@app.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    if not data.get('username') or not data.get('password'):
        return jsonify({'mensagem': 'Usuário e senha são obrigatórios!'}), 400

    user = db.usuario.find_one({'username': data['username']})
    if not user or not check_password_hash(user['password'], data['password']):
        return jsonify({'mensagem': 'Credenciais inválidas!'}), 401

    # Retorna também o username para salvar no localStorage
    return jsonify({
        'mensagem': 'Login realizado com sucesso!',
        'username': user['username']
    }), 200


@app.route('/listusers')
def list_users():
    """Lista todos os usuários"""
    users = db.usuario.find({})
    return flask.jsonify(json.loads(json_util.dumps(users)))

@app.route('/getuser/<string:userId>')
def get_user(userId):
    """Obtém um usuário pelo ID"""
    user = db.usuario.find_one({"_id": ObjectId(userId)})
    if user:
        return flask.jsonify(json.loads(json_util.dumps(user)))
    else:
        return jsonify(mensagem='Usuário não encontrado.'), 404

@app.route('/updateuser', methods=['POST'])
def update_user():
    json_data = request.json
    if json_data and db.usuario.find_one({"_id": ObjectId(json_data["id"])}):
        db.usuario.update_one(
            {'_id': ObjectId(json_data["id"])},
            {"$set": {
                'username': json_data["username"],
                'email': json_data["email"],
                'password': generate_password_hash(json_data["password"]),
                'foto': json_data.get("foto", "")
            }}
        )
        return jsonify(mensagem='Usuário atualizado com sucesso!')
    else:
        return jsonify(mensagem='Erro ao atualizar usuário.')


@app.route('/deleteuser/<string:userId>')
def delete_user(userId):
    """Deleta um usuário pelo ID"""
    result = db.usuario.delete_one({"_id": ObjectId(userId)})
    if result.deleted_count > 0:
        return jsonify(mensagem='Usuário removido com sucesso!')
    else:
        return jsonify(mensagem='Erro ao remover usuário.')

def carregar_generos():
    url = "https://api.themoviedb.org/3/genre/movie/list"
    params = {
        "api_key": TMDB_API_KEY,
        "language": "pt-BR"
    }
    resposta = requests.get(url, params=params)
    if resposta.status_code == 200:
        generos = resposta.json().get("genres", [])
        return {g["id"]: g["name"] for g in generos}
    return {}


@app.route('/tmdb')
def buscar_tmdb():
    query = request.args.get('q', '')
    if not query:
        return jsonify([])

    url = "https://api.themoviedb.org/3/search/multi"
    params = {
        "api_key": TMDB_API_KEY,
        "query": query,
        "language": "pt-BR"
    }

    response = requests.get(url, params=params)
    generos_map = carregar_generos()
    resultados = []

    if response.status_code == 200:
        for item in response.json().get("results", [])[:5]:
            if item.get("media_type") in ["movie", "tv"]:
                ids_generos = item.get("genre_ids", [])
                nomes_generos = [generos_map.get(gid) for gid in ids_generos if generos_map.get(gid)]
                resultados.append({
                    "titulo": item.get("title") or item.get("name"),
                    "tipo": "Filme" if item.get("media_type") == "movie" else "Série",
                    "descricao": item.get("overview", ""),
                    "ano": (item.get("release_date") or item.get("first_air_date") or "")[:4],
                    "genero": ", ".join(nomes_generos),
                    "avaliacao": "",
                    "imagem": f"https://image.tmdb.org/t/p/w500{item.get('poster_path')}" if item.get("poster_path") else ""
                })


    return jsonify(resultados)
