# verificacao manual, para saber se o JSON funcionava

from datetime import datetime

from src.modelo.mesa import Mesa
from src.modelo.cliente import Cliente
from src.modelo.reserva import Reserva
from src.serializacao import serializar_reserva, desserializar_reserva

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

# Serialização: guardar a reserva no ficheiro JSON
serializar_reserva(reserva)
print("Reserva guardada com sucesso!")

# Desserialização: recuperar a reserva do ficheiro JSON
reserva_recuperada = desserializar_reserva()

print("\nReserva recuperada:")
print(reserva_recuperada.para_dicionario())

print("\nTipo da data:")
print(type(reserva_recuperada.data_hora).__name__)
