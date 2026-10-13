def resumo_reserva_mesa(nome, pessoas, estado):
    nome_validacao = bool(nome.strip())
    pessoas_valido = 1 <= pessoas <= 12
    estado_valido = estado in ["confirmada", "pendente"]
    if not nome_validacao:
        nome_validacao = "Sem identificacao"
    else:
        nome_final=nome
    if 1 <= pessoas <= 12:
        pessoas_final = pessoas
    else:
        pessoas_final = 0  
 
    
    if estado in ["confirmada", "pendente"]:
        estado_final = estado
    else:
        estado_final = "invalido"
    
    return nome_final, pessoas_final, estado_final


nome, pessoas, estado = resumo_reserva_mesa("Ana Silva", 4, "confirmada")
 


print(f"Identificacao: {str(nome)} | Pessoas: {pessoas} | Estado: {estado}")
print(f"{'Nome':<20} {'Pessoas':<10} {'Estado':<10}")
print(f"{str(nome):<20} {str(pessoas):<10} {str(estado):<10}")

