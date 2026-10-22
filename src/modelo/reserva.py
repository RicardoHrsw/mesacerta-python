from src.modelo.mesa import Mesa
from src.modelo.cliente import Cliente
   
class Reserva:
    def __init__(self, mesa: Mesa, cliente: Cliente, num_pessoas: int):
        self.mesa = mesa
        self.num_pessoas = num_pessoas
        self.cliente = cliente
 
    def verificar_lotacao(self):
        return self.num_pessoas <= self.mesa.capacidade