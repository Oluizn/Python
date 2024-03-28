import random as rn

# Função para coeficientes de acertividade
def coeficiente(taxa):
    rando = rn.random()
    if rando < taxa:
        return True
    else:
        return False

# Função pra sair 1 rei
def prob_rei(ciclo):
    cartas_baralho = 52
    cartas_naipe = 4
    cont = 0
    for i in range(ciclo):
        rei = coeficiente(cartas_naipe / cartas_baralho)
        if rei:
            cont += 1
    return cont / ciclo

# Função para sair 2 reis em sequencia
def prob_rei_seq2(ciclo):
    cartas_baralho = 52
    cartas_naipe = 4
    cont = 0
    dois_reis = 0
    for i in range(ciclo):
        for j in range(2):
            rei = coeficiente(cartas_naipe / cartas_baralho)
            if rei:
                cont += 1
            else:
                cont = 0
                break
        if cont == 4:
            dois_reis += 1
    return dois_reis / ciclo

# Função para sair 2 reis em sequencia sem reposição de carta
def prob_rei_seq2_unreplaced(ciclo):
    cartas_baralho = 52
    cartas_naipe = 4
    cont = 0
    dois_reis = 0
    for i in range(ciclo):
        for j in range(2):
            rei = coeficiente(cartas_naipe / cartas_baralho)
            if rei:
                cont += 1
                cartas_baralho -= 1
                cartas_naipe -= 1
            else:
                cont = 0
                break
        if cont == 2:
            dois_reis += 1
        cartas_baralho = 52
        cartas_naipe = 4
    return dois_reis / ciclo

# Função para sair 4 reis em sequencia
def prob_rei_seq4(ciclo):
    cartas_baralho = 52
    cartas_naipe = 4
    cont = 0
    quatro_reis = 0
    for i in range(ciclo):
        for j in range(4):
            rei = coeficiente(cartas_naipe / cartas_baralho)
            if rei:
                cont += 1

            else:
                cont = 0
                break
        if cont == 4:
            quatro_reis += 1
    return quatro_reis / ciclo

# Função para sair 4 reis em sequencia sem reposição de carta
def prob_rei_seq4_unreplaced(ciclo):
    cartas_baralho = 52
    cartas_naipe = 4
    cont = 0
    quatro_reis = 0
    for i in range(ciclo):
        for j in range(4):
            rei = coeficiente(cartas_naipe / cartas_baralho)
            if rei:
                cont += 1
                cartas_baralho -= 1
                cartas_naipe -= 1
            else:
                cont = 0
                break
        if cont == 4:
            quatro_reis += 1
        cartas_baralho = 52
        cartas_naipe = 4
    return quatro_reis / ciclo

# Chamando as funções e dando o valor de iterações

ciclo = 10**6
print(f"probabilidade vim rei {prob_rei(ciclo)*100:.2f}%")
print(f"probabilidade vim 2 reis em sequencia {prob_rei_seq2(ciclo)*100:.4f}%")
print(f"probabilidade vim 2 reis em sequencia sem reposição{prob_rei_seq2_unreplaced(ciclo)*100:.4f}%")
print(f"probabilidade vim 4 reis em sequencia {prob_rei_seq4(ciclo)*100:.6f}%")
print(f"probabilidade vim 4 reis em sequencia sem reposição{prob_rei_seq4_unreplaced(ciclo)*100:.6f}%")
