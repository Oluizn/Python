import random as rn

# coeficientes de probabilidade das empresas
empresa_a = 0.4
empresa_b = 0.35
empresa_c = 0.25

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


# Função para verificar se foi ultrapassado os custos pela agência
def consultorias(ciclo, empresa, custo):
    cont = 0
    for i in range(ciclo):
        producao = coeficiente(empresa)  # Verifica qual empresa foi responsável
        if producao:
            if coeficiente(custo):  # Verifica se ultrapassou os custos
                cont += 1
    return cont / ciclo


ciclo = 10**6


# Atribuindo a quantidade de vezes que cada empresa ultrapassou os custos a uma variável
quantidade_empresa_a = consultorias(ciclo, empresa_a, custo_a)
quantidade_empresa_b = consultorias(ciclo, empresa_b, custo_b)
quantidade_empresa_c = consultorias(ciclo, empresa_c, custo_c)

# Calculando a probabilidade de cada empresa ultrapassar os custo, fazendo a quantidade individual divido pelo numero total somado das 3 empresas
prob_empresa_a = quantidade_empresa_a / (quantidade_empresa_a + quantidade_empresa_b + quantidade_empresa_c)
prob_empresa_b = quantidade_empresa_b / (quantidade_empresa_a + quantidade_empresa_b + quantidade_empresa_c)
prob_empresa_c = quantidade_empresa_c / (quantidade_empresa_a + quantidade_empresa_b + quantidade_empresa_c)

print(f"A probabilidade da consultoria A é de {prob_empresa_a*100:.2f}%")
print(f"A probabilidade da consultoria B é de {prob_empresa_b*100:.2f}%")
print(f"A probabilidade da consultoria C é de {prob_empresa_c*100:.2f}%")
