class Mesa:
    def __init__(self, numero, capacidade, estado):
        self.numero = numero
        self.capacidade = capacidade
        self.estado = estado


    @property
    def capacidade(self):
        return self._capacidade

    @capacidade.setter
    def capacidade(self, valor):
        if valor <=0:
            raise ValueError("A capacidade da mesa deve ser um valor positivo.")
        self._capacidade=valor