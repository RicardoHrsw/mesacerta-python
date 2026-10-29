class Cliente:
    def __init__(self, nome, contacto=None, historico=None):
        self.nome = nome
        self.contacto = contacto
        self.historico = historico

    def para_dicionario(self):
        return {
            "nome": self.nome,
            "contacto": self.contacto,
            "historico": self.historico
        }

    @classmethod
    def de_dicionario(cls, dados):
        return cls(
            nome=dados["nome"],
            contacto=dados.get("contacto"),
            historico=dados.get("historico")
        )
