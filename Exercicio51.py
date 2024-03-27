import random

# Função para calcular probabilidade de retirar 1 rei
def probabilidade_rei(ciclo, rei):
    vezes_numero_aparece = 0
    cartas_no_baralho = 52  # Total de cartas no baralho
    cartas_por_naipe = 4  # Cartas iguais com naipe diferente (por exemplo, 4 reis)
    for i in range(ciclo):
        resultado = random.randint(1, cartas_no_baralho // cartas_por_naipe)  # Simulando retirada de cartas, como são 52 cartas e cada carta possui 4 variações, totaliza 13 de espaço amostral
        if resultado == rei:
            vezes_numero_aparece += 1
    return vezes_numero_aparece / ciclo

# Função para calcular a probabilidade para retirar 2 reis em sequência, com reposição da carta rei ao ser sorteada
def probabilidade_rei_sequencia2(ciclo, rei):
    vezes_numero_aparece = 0
    cartas_no_baralho = 52  # Total de cartas no baralho
    cartas_por_naipe = 4    # Cartas iguais com naipe diferente (por exemplo, 4 reis)

    for i in range(ciclo):
        sequencia_reis = 0
        for j in range(2):  # Procurando por uma sequência de 2 reis
            resultado = random.randint(1, cartas_no_baralho // cartas_por_naipe)
            if resultado == rei:
                sequencia_reis += 1
            else:
                sequencia_reis = 0
                break

        if sequencia_reis == 2:  # Se encontramos uma sequência de 2 reis
            vezes_numero_aparece += 1

    return vezes_numero_aparece / ciclo

# Função para retirar 4 reis em sequência, com reposição das cartas rei sorteadas
def probabilidade_rei_sequencia4(ciclo, rei):
    vezes_numero_aparece = 0
    cartas_no_baralho = 52  # Total de cartas no baralho
    cartas_por_naipe = 4    # Cartas iguais com naipe diferente (por exemplo, 4 reis)

    for i in range(ciclo):
        sequencia_reis = 0
        for j in range(4):  # Procurando por uma sequência de quatro reis
            resultado = random.randint(1, cartas_no_baralho // cartas_por_naipe)
            if resultado == rei:
                sequencia_reis += 1
            else:
                sequencia_reis = 0
                break

        if sequencia_reis == 4:  # Se encontrarmos uma sequência de 4 reis
            vezes_numero_aparece += 1

    return vezes_numero_aparece / ciclo

# Função para retirar 2 reis em sequência, sem reposição das cartas reis sortedas
def probabilidade_rei_sequencia2_unreplaced(ciclo, lista_rei):
    vezes_numero_aparece = 0
    cartas_no_baralho = 52  # Total de cartas no baralho

    for i in range(ciclo):
        sequencia_reis = 0
        cartas_restantes = cartas_no_baralho

        for j in range(2):  # Procurando por uma sequência de dois reis
            resultado = random.randint(1, cartas_restantes)

            if resultado in lista_rei:  # sair um rei
                sequencia_reis += 1
                cartas_restantes -= 1
            else:
                sequencia_reis = 0
                break

        if sequencia_reis == 2:  # Se encontrarmos uma sequência de 2 reis
            vezes_numero_aparece += 1

    return vezes_numero_aparece / ciclo

# Função para retirar 4 reis em sequência, sem reposição das cartas reis sortedas
def probabilidade_rei_sequencia4_unreplaced(ciclo, lista_rei):
    vezes_numero_aparece = 0
    cartas_no_baralho = 52  # Total de cartas no baralho

    for i in range(ciclo):
        sequencia_reis = 0
        cartas_restantes = cartas_no_baralho

        for j in range(4):  # Procurando por uma sequência de quatro reis
            resultado = random.randint(1, cartas_restantes)

            if resultado in lista_rei:  # sair um rei
                sequencia_reis += 1
                cartas_restantes -= 1
            else:
                sequencia_reis = 0
                break

        if sequencia_reis == 4:  # Se encontrarmos uma sequência de 4 reis
            vezes_numero_aparece += 1

    return vezes_numero_aparece / ciclo

# Definindo o número ciclos
ciclo = 1000000

# Número específico referente à carta rei
carta_rei = 13  # Para quando as cartas são repostas no baralho
lista_rei = [49, 50, 51, 52]    # Para quando as cartas não são repostas no baralho

# Chamando as funções para calcular a probabilidade de sair a carta rei
probabilidade = probabilidade_rei(ciclo, carta_rei)
probabilidade_em_sequencia2 = probabilidade_rei_sequencia2(ciclo, carta_rei)
probabilidade_em_sequencia4 = probabilidade_rei_sequencia4(ciclo, carta_rei)
probabilidade_em_sequencia2_unreplaced = probabilidade_rei_sequencia2_unreplaced(ciclo, lista_rei)
probabilidade_em_sequencia4_unreplaced = probabilidade_rei_sequencia4_unreplaced(ciclo, lista_rei)
print(f"A probabilidade de sair a carta rei em {ciclo} ciclos é de aproximadamente {probabilidade*100:.10f}%")
print(f"A probabilidade de sair a carta rei duas vezes seguidas, com a carta rei sendo reposta no baralho, em {ciclo} ciclos é de aproximadamente {probabilidade_em_sequencia2*100:.10f}%")
print(f"A probabilidade de sair a carta rei quatro vezes seguidas, com a carta rei sendo reposta no baralho, em {ciclo} ciclos é de aproximadamente {probabilidade_em_sequencia4*100:.10f}%")
print(f"A probabilidade de sair a carta rei 2 vezes seguidas, com a carta rei nao sendo reposta no baralho, em {ciclo} ciclos é de aproximadamente {probabilidade_em_sequencia2_unreplaced*100:.10f}%")
print(f"A probabilidade de sair a carta rei 4 vezes seguidas, com a carta rei nao sendo reposta no baralho, em {ciclo} ciclos é de aproximadamente {probabilidade_em_sequencia4_unreplaced*100:.10f}%")
