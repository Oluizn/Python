import random as rn


# coeficientes de probabilidade das empresas
agencia_a = 0.4
agencia_b = 0.35
agencia_c = 0.25

# coeficiente de probabilidade de cada empresa ultrapassar os custos
custo_a = 0.05
custo_b = 0.03
custo_c = 0.15


# Função para gerar um número aleatório entre 0 e 1
def coeficiente(taxa):
    rando = rn.random()
    if rando < taxa:
        return True
    else:
        return False


def consultorias(ciclo, agencia, custo):
    cont = 0
    for i in range(ciclo):
        producao = coeficiente(agencia)  # Verifica qual agencia responsável
        if producao:
            if coeficiente(custo):  # Verifica se ultrapassou os custos
                cont += 1
    return cont / ciclo


ciclo = 10**6


# Atribuindo a quantidade de vezes que cada empresa ultrapassou os custos a uma variável
quantidade_agencia_a = consultorias(ciclo, agencia_a, custo_a)
quantidade_agencia_b = consultorias(ciclo, agencia_b, custo_b)
quantidade_agencia_c = consultorias(ciclo, agencia_c, custo_c)

#Calculando a probabilidade de cada empresa ultrapassar os custo, fazendo a quantidade individual divido pelo numero total somado das 3 empresas
prob_agencia_a = quantidade_agencia_a / (quantidade_agencia_a + quantidade_agencia_b + quantidade_agencia_c)
prob_agencia_b = quantidade_agencia_b / (quantidade_agencia_a + quantidade_agencia_b + quantidade_agencia_c)
prob_agencia_c = quantidade_agencia_c / (quantidade_agencia_a + quantidade_agencia_b + quantidade_agencia_c)

print(f"A probabilidade da consultoria A é de {prob_agencia_a*100:.2f}%")
print(f"A probabilidade da consultoria B é de {prob_agencia_b*100:.2f}%")
print(f"A probabilidade da consultoria C é de {prob_agencia_c*100:.2f}%")