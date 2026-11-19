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

    campos = ("numero", "capacidade", "estado")
    em_falta = [campo for campo in campos if campo not in dados]
    if em_falta:
        return jsonify({"erro": f"Campos em falta: {', '.join(em_falta)}"}), 400

    try:
        mesa = Mesa.de_dicionario(dados)
    except (ValueError, TypeError) as erro:
        return jsonify({"erro": str(erro)}), 400

    numeros_existentes = [numero for numero, _, _ in listar_mesas(CAMINHO)]
    if mesa.numero in numeros_existentes:
        return jsonify({"erro": f"A mesa {mesa.numero} já existe"}), 409

    adicionar_mesa(mesa, CAMINHO)
    return jsonify(mesa.para_dicionario()), 201


