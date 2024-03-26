import random

def probabilidade_rei(ciclo, rei):
    vezes_numero_aparece = 0
    for i in range(ciclo):
        resultado = random.randint(1, 13)  # Simulando retirada de cartas, como são 52 cartas e cada carta possui 4 variações, totaliza 13 de espaço amostral
        if resultado == rei:
            vezes_numero_aparece += 1
    return vezes_numero_aparece / ciclo

def probabilidade_rei_sequencia2(ciclo, rei):
    vezes_numero_aparece = 0
    for i in range(ciclo):
        resultado = random.randint(1, 13)  # Simulando retirada de cartas, como são 52 cartas e cada carta possui 4 variações, totaliza 13 de espaço amostral
        if resultado == rei:
            resultado = random.randint(1, 13)
            if resultado == rei:    #condição para vim dois reis em seguida com a primeira carta rei sendo reposta no baralho
                vezes_numero_aparece += 1
    return vezes_numero_aparece / ciclo

def probabilidade_rei_sequencia4(ciclo, rei):
    vezes_numero_aparece = 0
    for i in range(ciclo):
        resultado = random.randint(1, 13)  # Simulando retirada de cartas, como são 52 cartas e cada carta possui 4 variações, totaliza 13 de espaço amostral
        if resultado == rei:
            resultado = random.randint(1, 13)
            if resultado == rei:    #condição para vim dois reis em seguida com a carta rei sendo reposta no baralho
                resultado = random.randint(1, 13)
                if resultado == rei:    #condição para vim tres reis em seguida com a carta rei sendo reposta no baralho
                    resultado = random.randint(1, 13)
                    if resultado == rei:    #condição para vim quatro reis em seguida com a carta rei sendo reposta no baralho
                        vezes_numero_aparece += 1
    return vezes_numero_aparece / ciclo

# Defina o número ciclos
ciclo = 10000000

# Número específico referente à carta rei
carta_rei = 13

# Calcule a probabilidade de sair o número específico
probabilidade = probabilidade_rei(ciclo, carta_rei)
probabilidade_em_sequencia2 = probabilidade_rei_sequencia2(ciclo, carta_rei)
probabilidade_em_sequencia4 = probabilidade_rei_sequencia4(ciclo, carta_rei)
print(f"A probabilidade de sair a carta rei em {ciclo} ciclos é de aproximadamente {probabilidade*100:.10f}%")
print(f"A probabilidade de sair a carta rei duas vezes seguidas, com a carta rei sendo reposta no baralho, em {ciclo} ciclos é de aproximadamente {probabilidade_em_sequencia2*100:.10f}%")
print(f"A probabilidade de sair a carta rei quatro vezes seguidas, com a carta rei sendo reposta no baralho, em {ciclo} ciclos é de aproximadamente {probabilidade_em_sequencia4*100:.10f}%")
