from src.modelo.mesa import Mesa
from src.modelo.cliente import Cliente
from datetime import datetime


class Reserva:
    def __init__(self, mesa: Mesa, num_pessoas: int, cliente: Cliente = None, data_hora: datetime = None, estado: str = "Pendente"):
        self.mesa = mesa
        self.num_pessoas = num_pessoas
        self.cliente = cliente
        self.data_hora = data_hora
        self.estado = estado

    def verificar_lotacao(self):
        return self.num_pessoas <= self.mesa.capacidade

    def para_dicionario(self):
        return {
            "mesa": self.mesa.para_dicionario(),
            "num_pessoas": self.num_pessoas,
            "cliente": (
                self.cliente.para_dicionario()
                if self.cliente is not None
                else None
            ),
            "data_hora": (
                self.data_hora.isoformat()
                if self.data_hora is not None
                else None
            ),
            "estado": self.estado
        }

    @classmethod
    def de_dicionario(cls, dados):
        return cls(
            mesa=Mesa.de_dicionario(dados["mesa"]),
            num_pessoas=dados["num_pessoas"],
            cliente=(
                Cliente.de_dicionario(dados["cliente"])
                if dados.get("cliente") is not None
                else None
            ),
            data_hora=(
                datetime.fromisoformat(dados["data_hora"])
                if dados.get("data_hora") is not None
                else None
            ),
            estado=dados.get("estado", "Pendente")
        )
