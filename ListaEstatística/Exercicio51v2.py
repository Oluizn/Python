import random as rn

ciclo = 10**6   # Quantidade de iterações


# Função para coeficientes de acertividade
def coeficiente(taxa):
    rando = rn.random()
    if rando < taxa:
        return True
    else:
        return False


# Função para sair 1 rei
def prob_rei(ciclo):
    cartas_baralho = 52
    cartas_naipe = 4
    cont = 0
    for i in range(ciclo):
        rei = coeficiente(cartas_naipe / cartas_baralho)
        if rei:
            cont += 1
    return cont / ciclo


# Função para sair 2 reis em sequência
def prob_rei_seq2(ciclo):
    cartas_baralho = 52
    cartas_naipe = 4
    cont = 0    # contador a ser incrementado caso um rei seja retirado
    dois_reis = 0   # contador a ser incrementado casa dois reis em sequência seja encontrado
    const_comparativa = 2  # constando para loop e condição de incremento para a variável dois_reis
    for i in range(ciclo):
        for j in range(const_comparativa):
            # Loop aninhado para tentar encontrar dois reis em sequência
            rei = coeficiente(cartas_naipe / cartas_baralho)
            if rei:
                cont += 1
            else:
                cont = 0
                # Caso não encontre rei na primeira tentativa, sair do loop
                break
        # Condicional para verificar se foi encontrado dois reis em sequência
        if cont == const_comparativa:
            dois_reis += 1
    return dois_reis / ciclo


# Função para sair 2 reis em sequência sem reposição de carta
def prob_rei_seq2_unreplaced(ciclo):
    cartas_baralho = 52
    cartas_naipe = 4
    cont = 0  # contador a ser incrementado caso um rei seja retirado
    dois_reis = 0  # contador a ser incrementado casa dois reis em sequência seja encontrado
    const_comparativa = 2  # constando para loop e condição de incremento para a variável dois_reis
    for i in range(ciclo):
        for j in range(const_comparativa):
            rei = coeficiente(cartas_naipe / cartas_baralho)
            if rei:
                cont += 1
                cartas_baralho -= 1     # Subtrai uma carta do baralho
                cartas_naipe -= 1       # Subtrai uma carta do naipe desejado
            else:
                cont = 0
                # Caso não encontre rei na primeira tentativa, sair do loop
                break
        # Condicional para verificar se foi encontrado dois reis em sequência
        if cont == const_comparativa:
            dois_reis += 1
        # Devolve valores originais às variáveis
        cartas_baralho = 52
        cartas_naipe = 4
    return dois_reis / ciclo


# Função para sair 4 reis em sequência
def prob_rei_seq4(ciclo):
    cartas_baralho = 52
    cartas_naipe = 4
    cont = 0        # contador a ser incrementado caso um rei seja retirado
    quatro_reis = 0     # contador a ser incrementado casa quatro reis em sequência seja encontrado
    const_comparativa = 4       # constando para loop e condição de incremento para a variável
    for i in range(ciclo):
        for j in range(const_comparativa):
            rei = coeficiente(cartas_naipe / cartas_baralho)
            if rei:
                cont += 1
            else:
                cont = 0
                # Caso não encontre rei na primeira tentativa, sair do loop
                break
        # Condicional para verificar se foi encontrado quatro reis em sequência
        if cont == const_comparativa:
            quatro_reis += 1
    return quatro_reis / ciclo


# Função para sair 4 reis em sequência sem reposição de carta
def prob_rei_seq4_unreplaced(ciclo):
    cartas_baralho = 52
    cartas_naipe = 4
    cont = 0        # contador a ser incrementado caso um rei seja retirado
    quatro_reis = 0     # contador a ser incrementado casa quatro reis em sequência seja encontrado
    const_comparativa = 4  # constando para loop e condição de incremento para a variável
    for i in range(ciclo):
        for j in range(const_comparativa):
            rei = coeficiente(cartas_naipe / cartas_baralho)
            if rei:
                cont += 1
                cartas_baralho -= 1  # Subtrai uma carta do baralho
                cartas_naipe -= 1  # Subtrai uma carta do naipe desejado
            else:
                cont = 0
                # Caso não encontre rei na primeira tentativa, sair do loop
                break
        if cont == const_comparativa:
            quatro_reis += 1
        # Devolve valores originais às variáveis
        cartas_baralho = 52
        cartas_naipe = 4
    return quatro_reis / ciclo


# Chamando as funções
print(f"probabilidade vim rei {prob_rei(ciclo)*100:.2f}%")
print(f"probabilidade vim 2 reis em sequencia {prob_rei_seq2(ciclo)*100:.4f}%")
print(f"probabilidade vim 2 reis em sequencia sem reposição {prob_rei_seq2_unreplaced(ciclo)*100:.4f}%")
print(f"probabilidade vim 4 reis em sequencia {prob_rei_seq4(ciclo)*100:.6f}%")
print(f"probabilidade vim 4 reis em sequencia sem reposição {prob_rei_seq4_unreplaced(ciclo)*100:.6f}%")
