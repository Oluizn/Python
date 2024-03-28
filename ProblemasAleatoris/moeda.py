import random

def probabilidade_cara(num_lancamentos):
    caras = 0
    for _ in range(num_lancamentos):
        resultado = random.choice(['cara', 'coroa'])
        if resultado == 'cara':
            caras += 1
    return caras / num_lancamentos

# Defina o número de lançamentos da moeda
num_lancamentos = 1000

# Calcule a probabilidade de sair cara
probabilidade = probabilidade_cara(num_lancamentos)
print(f"A probabilidade de sair cara em {num_lancamentos} lançamentos é de aproximadamente {probabilidade:.2f}")
