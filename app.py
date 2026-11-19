from flask import Flask, jsonify
from src.modelo.mesa import Mesa
from src.base_dados import criar_tabela, listar_mesas, adicionar_mesa




app = Flask (__name__)
CAMINHO = "dados/mesacerta.db"

criar_tabela()

@app.get("/mesas")
def get_mesas():
    registos = listar_mesas(CAMINHO)

    mesas_json =[
        {
            "numero": numero, 
            "capacidade": capacidade, 
            "estado": estado,
            }
            for numero, capacidade, estado in registos
    ]

    return jsonify(mesas_json), 200

@app.post("/mesas")
def post_mesas():
    dados = request.get_json(silent=True)
    if not isinstance(dados, dict):
        return jsonify({"erro": "JSON invalido"}), 400


