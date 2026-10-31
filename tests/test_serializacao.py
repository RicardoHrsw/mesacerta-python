import unittest
import tempfile
from pathlib import Path
from datetime import datetime

from src.modelo.mesa import Mesa
from src.modelo.reserva import Reserva
from src.modelo.cliente import Cliente
from src.serializacao import serializar_reserva, desserializar_reserva


class TestSerializacao(unittest.TestCase):

    def test_guardar_e_recuperar(self):
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "reservas.json"

            cliente = Cliente("Diana", "932450320")
            mesa = Mesa(1, 4, "Disponível")
            data_hora = datetime(2026, 11, 14, 19, 30)

            reserva = Reserva(
                mesa=mesa,
                num_pessoas=3,
                cliente=cliente,
                data_hora=data_hora,
                estado="confirmado"
            )

            serializar_reserva(reserva, caminho)
            recuperada = desserializar_reserva(caminho)

            self.assertEqual(type(recuperada), Reserva)
            self.assertEqual(recuperada.num_pessoas, 3)
            self.assertEqual(recuperada.cliente.nome, "Diana")
            self.assertEqual(recuperada.mesa.capacidade, 4)
            self.assertEqual(recuperada.estado, "confirmado")
            self.assertEqual(recuperada.data_hora, data_hora)

    def test_reserva_invalida(self):
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "reservas.json"

            caminho.write_text(
                '''
                {
                    "mesa": {
                        "numero": 1,
                        "capacidade": 0,
                        "estado": "Disponível"
                    },
                    "num_pessoas": 3,
                    "cliente": null,
                    "data_hora": null,
                    "estado": "confirmado"
                }
                ''',
                encoding="utf-8"
            )

            with self.assertRaises(ValueError):
                desserializar_reserva(caminho)


if __name__ == "__main__":
    unittest.main()
