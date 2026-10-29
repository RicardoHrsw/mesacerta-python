from datetime import datetime
from src.modelo.mesa import Mesa
from src.modelo.reserva import Reserva
from src.reservas_mesas import mostrar_reserva
from src.modelo.cliente import Cliente


def main():
    cliente_1 = Cliente(nome="Diana", contacto="932450320")
    cliente_2 = Cliente(nome="Tiago", contacto="924509120")

    mesa_1 = Mesa(numero=1, capacidade=4, estado="Disponivel")
    mesa_2 = Mesa(numero=2, capacidade=2, estado="Disponivel")

    data_hora_reserva = datetime(2026, 11, 14, 19, 30)

    reserva_compativel = Reserva(
        mesa_1, 3, cliente_1, data_hora=data_hora_reserva, estado="confirmado")
    reserva_excede = Reserva(mesa_2, 6, cliente_2,
                             data_hora=data_hora_reserva, estado="pendente")

    mostrar_reserva(reserva_compativel)
    mostrar_reserva(reserva_excede)


if __name__ == "__main__":
    main()
