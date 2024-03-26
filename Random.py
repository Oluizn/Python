import random


def simular_lancamento_de_dado():
    # Gerar um número aleatório entre 1 e 6 (representando as faces do dado)
    return random.randint(1, 6)


def calcular_probabilidade_de_impar(n_lancamentos):
    # Contador para armazenar o número de vezes que obtemos um número ímpar
    contador_impar = 0

    for _ in range(n_lancamentos):
        resultado_lancamento = simular_lancamento_de_dado()
        # Verificar se o resultado é ímpar (1, 3 ou 5)
        if resultado_lancamento % 2 != 0:
            contador_impar += 1

    # Calcular a probabilidade dividindo o número de resultados ímpares pelo número total de lançamentos
    probabilidade_impar = contador_impar / n_lancamentos
    return probabilidade_impar


# Definir o número de lançamentos para simular
numero_de_lancamentos = 10000

# Calcular e imprimir a probabilidade de obter um número ímpar
probabilidade = calcular_probabilidade_de_impar(numero_de_lancamentos)
print(f"A probabilidade de obter um número ímpar em {numero_de_lancamentos} lançamentos é aproximadamente {probabilidade:.2f}")
