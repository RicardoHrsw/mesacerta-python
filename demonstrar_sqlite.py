from pathlib import Path
from src.modelo.mesa import Mesa
from src.base_dados import (
    criar_tabela,
    adicionar_mesa,
    listar_mesas
)


CAMINHO = "dados/mesacerta.db"


def demonstrar():
    criar_tabela(CAMINHO)
    mesa_1 = Mesa(1, 4, "Livre")
    mesa_2 = Mesa(2, 6, "Ocupada")

    adicionar_mesa(mesa_1, CAMINHO)
    adicionar_mesa(mesa_2, CAMINHO)

    print(f"A base de dados: {Path(CAMINHO).resolve()}")
    print("Mesas registadas: ")
    for numero, capacidade, estado in listar_mesas(CAMINHO):
        print(f"Mesa: {numero}| Capacidade: {capacidade} | Estado: {estado}")


if __name__ == "__main__":
    demonstrar()
