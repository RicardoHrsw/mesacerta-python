def resumo_reserva_mesa(nome, pessoas, estado):
    nome_validacao = bool(nome.strip())
    pessoas_valido = 1 <= pessoas <= 12
