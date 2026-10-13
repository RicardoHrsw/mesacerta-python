import unittest

from src.reservas_mesas import resumo_reserva_mesa


class TestProjeto(unittest.TestCase):
    def test_caso_valido(self):
        resultado = resumo_reserva_mesa("João", 4, "confirmada")
        self.assertEqual(resultado, ("João", 4, "confirmada"))
