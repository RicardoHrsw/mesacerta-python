import unittest
from src.reservas_mesas import resumo_reserva_mesa


class TestProjeto(unittest.TestCase):
    def test_caso_valido(self):
        resultado = resumo_reserva_mesa("João", 4, "confirmada")
        self.assertEqual(resultado, ("João", 4, "confirmada"))


    def test_caso_pessoas_invalido(self):
        resultado = resumo_reserva_mesa("João", 15, "confirmada")
        self.assertEqual(resultado, ("João", 0, "confirmada"))


    def test_caso_estado_invalido(self):
        resultado = resumo_reserva_mesa("Ana", 2, "cancelada")
        self.assertEqual(resultado, ("Ana", 2, "invalido"))
