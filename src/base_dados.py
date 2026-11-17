import sqlite3
from contextlib import closing


def criar_tabela(caminho):
    with closing(sqlite3.connect(caminho)) as ligacao:
        with ligacao:
            ligacao.execute(
                """
                CREATE TABLE IF NOT EXISTS mesas (
                    numero     INTEGER PRIMARY KEY,
                    capacidade INTEGER NOT NULL,
                    estado     TEXT NOT NULL
                )
                """
            )


def adicionar_mesa(mesa, caminho):
    with closing(sqlite3.connect(caminho)) as ligacao:
        with ligacao:
            ligacao.execute(
                "INSERT OR REPLACE INTO mesas (numero, capacidade, estado) "
                "VALUES (?, ?, ?)",
                (mesa.numero, mesa.capacidade, mesa.estado),
            )


def listar_mesas(caminho):
    with closing(sqlite3.connect(caminho)) as ligacao:
        cursor = ligacao.execute(
            "SELECT numero, capacidade, estado FROM mesas ORDER BY numero"
        )
        return cursor.fetchall()
