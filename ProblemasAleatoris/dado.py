import random

def probabilidade_numero(num_lancamentos, numero):
    vezes_numero_aparece = 0
    for _ in range(num_lancamentos):
        resultado = random.randint(1, 6)  # Simulando o lançamento de um dado de seis lados
        if resultado == numero:
            vezes_numero_aparece += 1
    return vezes_numero_aparece / num_lancamentos

# Defina o número de lançamentos do dado
num_lancamentos = 1000

# Número específico que você quer calcular a probabilidade
numero_especifico = 3

# Calcule a probabilidade de sair o número específico
probabilidade = probabilidade_numero(num_lancamentos, numero_especifico)
print(f"A probabilidade de sair o número {numero_especifico} em {num_lancamentos} lançamentos é de aproximadamente {probabilidade:.2f}")
