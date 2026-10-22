from src.modelo.mesa import Mesa
from src.modelo.reserva import Reserva


def mostrar_reserva(reserva):
    mesa = reserva.mesa
    print(f"Mesa {mesa.numero} (capacidade: {mesa.capacidade}) | Pessoas: {reserva.num_pessoas}")
    if reserva.verificar_lotacao():
        print("-> Reserva compatível: a mesa comporta o pedido.\n")
    else:
        print("-> Reserva recusada: o número de pessoas excede a capacidade da mesa.\n")


def main():
    mesa = Mesa(1, 4)

    reserva_compativel = Reserva(mesa, 3)
    reserva_excede = Reserva(mesa, 6)

    mostrar_reserva(reserva_compativel)
    mostrar_reserva(reserva_excede)


if __name__ == "__main__":
    main()
