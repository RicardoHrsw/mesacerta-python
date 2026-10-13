def resumo_reserva_mesa(nome, pessoas, estado):
    nome_validacao = bool(nome.strip())
    pessoas_valido = 1 <= pessoas <= 12
    estado_valido = estado in ["confirmada", "pendente"]

    return (nome, pessoas, estado) if nome_validacao and pessoas_valido and estado_valido else None
