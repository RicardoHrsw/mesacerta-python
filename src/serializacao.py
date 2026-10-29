import json
from pathlib import Path

from src.modelo.reserva import Reserva

caminho = Path(__file__).parent / "reservas.json"


def serializar_reserva(reserva):
    dados = reserva.para_dicionario()

    with caminho.open("w", encoding="utf-8") as ficheiro:
        json.dump(
            dados,
            ficheiro,
            ensure_ascii=False,
            indent=4
        )


def desserializar_reserva():
    with caminho.open("r", encoding="utf-8") as ficheiro:
        dados = json.load(ficheiro)

    return Reserva.de_dicionario(dados)
