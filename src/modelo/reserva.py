from src.modelo.mesa import Mesa
from src.modelo.cliente import Cliente
from datetime import datetime
   
class Reserva:
    def __init__(self, mesa: Mesa, cliente: Cliente, num_pessoas: int, data_hora: datetime, estado: str="Pendente"):
        self.mesa = mesa
        self.num_pessoas = num_pessoas
        self.cliente = cliente
        self.data_hora = data_hora
        self.estado = estado
 
    def verificar_lotacao(self):
        return self.num_pessoas <= self.mesa.capacidade