from src.modelo.mesa import Mesa
from src.modelo.reserva import Reserva
from src.reservas_mesas import mostrar_reserva
from src.modelo.cliente import Cliente

cliente_1 = Cliente("Diana")
cliente_2 = Cliente("Tiago")

mesa_1 = Mesa(1, 4, "Disponivel")
mesa_2 = Mesa(2, 2, "Disponivel")

reserva_compativel = Reserva(mesa_1, 3, cliente_1)
reserva_excede = Reserva(mesa_2, 6, cliente_2)

mostrar_reserva(reserva_compativel)
mostrar_reserva(reserva_excede)




