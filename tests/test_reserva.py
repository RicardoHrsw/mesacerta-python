import unittest
from src.modelo.mesa import Mesa
from src.modelo.reserva import Reserva
from src.modelo.cliente import Cliente
from datetime import datetime


class TestReserva(unittest.TestCase):
    def setUp(self):
        self.cliente = Cliente("Ana Silva")
        self.mesa = Mesa(1, 4, "Disponivel")
        self.data_hora = datetime(2026, 11, 5, 19, 30)

    def test_reserva_compativel(self):

        reserva = Reserva(
            mesa=self.mesa, num_pessoas=3, cliente=self.cliente, data_hora=self.data_hora, estado="confirmado")
        self.assertTrue(reserva.verificar_lotacao())

    def test_reserva_incompativel(self):
        reserva = Reserva(
            mesa=self.mesa, num_pessoas=6, cliente=self.cliente, data_hora=self.data_hora, estado="confirmado")
        self.assertFalse(reserva.verificar_lotacao())


if __name__ == "__main__":
    unittest.main()
