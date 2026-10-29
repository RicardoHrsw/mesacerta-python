def resumo_reserva_mesa(nome, pessoas, estado):
    nome_validacao = bool(nome.strip())
    pessoas_valido = 1 <= pessoas <= 12
    estado_valido = estado in ["confirmada", "pendente"]
    if not nome_validacao:
        nome_validacao = "Sem identificacao"
    else:
        nome_final=nome
    if pessoas_valido:
        pessoas_final = pessoas
    else:
        pessoas_final = 0  
 
    
    if estado_valido:
        estado_final = estado
    else:
        estado_final = "invalido"
    
    return nome_final, pessoas_final, estado_final


def mostrar_reserva(reserva):
    mesa = reserva.mesa
    print(f"Mesa {mesa.numero} (capacidade: {mesa.capacidade}) | Pessoas: {reserva.num_pessoas}")

 
    print(f"Identificacao: {str(reserva.cliente.nome)} | Pessoas: {reserva.num_pessoas} | Estado: {reserva.estado}")
    print(f"{'Nome':<20} {'Pessoas':<10} {'Estado':<10}")
    print(f"{str(reserva.cliente.nome):<20} {str(reserva.num_pessoas):<10} {str(reserva.estado):<10}")

    if reserva.verificar_lotacao():
        print("Reserva compatível: a mesa comporta o pedido.\n")
    else:
        print("Reserva recusada: o número de pessoas excede a capacidade maxima.\n")
