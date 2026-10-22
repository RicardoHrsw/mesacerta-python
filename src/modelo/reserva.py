from src.modelo.mesa import Mesa
   
class Reserva:
    def __init__(self, mesa: Mesa, num_pessoas: int):
        self.mesa = mesa
        self.num_pessoas = num_pessoas
 
    def verificar_lotacao(self):
        return self.num_pessoas <= self.mesa.capacidade