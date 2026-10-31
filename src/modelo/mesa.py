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
        if valor <= 0:
            raise ValueError(
                "A capacidade da mesa deve ser um valor positivo.")
        self._capacidade = valor

    def para_dicionario(self):
        return {
            "numero": self.numero,
            "capacidade": self.capacidade,
            "estado": self.estado
        }

    @classmethod
    def de_dicionario(cls, dados):
        return cls(
            numero=dados["numero"],
            capacidade=dados["capacidade"],
            estado=dados["estado"]
        )
