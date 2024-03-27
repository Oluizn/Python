import random as rn

# Coeficientes de produção de cada fábrica
prod_a = 0.15
prod_b = 0.35
prod_c = 0.5

# Coeficientes de defeito de cada fábrica
defeito_a = 0.01
defeito_b = 0.05
defeito_c = 0.02

# Função para gerar um número aleatório entre 0 e 1
def coeficiente(taxa):
    rando = rn.random()
    if rando < taxa:
        return True
    else:
        return False

# Função para verificar se houve defeito
def defeito(ciclo, fabrica, defeito):
    cont = 0
    for i in range(ciclo):
        producao = coeficiente(fabrica)    # Verifica se foi produzido na fábrica de acordo com o coeficiente de produção por fábrica
        if producao:
            if coeficiente(defeito):    # Verifica se houve defeito de acordo com o coeficiente de defeito
                cont += 1
    return cont / ciclo

# definindo variável de repetição
ciclo = 10000000

# Chamando as funções com respectiva quantidade de peças com defeito por fábrica
defeito_fabrica_a = defeito(ciclo, prod_a, defeito_a)   # 15000
defeito_fabrica_b = defeito(ciclo, prod_b, defeito_b)   # 175000
defeito_fabrica_c = defeito(ciclo, prod_c, defeito_c)   # 100000

# Calculando a probabilidade de defeito por fábrica fazendo a quantidade de defeito dividido pelo numero total de defeito somado de todas as fábricas
probabilidade_defeito_fabrica_a = defeito_fabrica_a / (defeito_fabrica_a + defeito_fabrica_b + defeito_fabrica_c)
probabilidade_defeito_fabrica_b = defeito_fabrica_b / (defeito_fabrica_a + defeito_fabrica_b + defeito_fabrica_c)
probabilidade_defeito_fabrica_c = defeito_fabrica_c / (defeito_fabrica_a + defeito_fabrica_b + defeito_fabrica_c)
print(f"A probabilidade da peças defeituosa ser da fabrica A é de {probabilidade_defeito_fabrica_a*100:.10f}")
print(f"A probabilidade da peças defeituosa ser da fabrica B é de {probabilidade_defeito_fabrica_b*100:.10f}")
print(f"A probabilidade da peças defeituosa ser da fabrica C é de {probabilidade_defeito_fabrica_c*100:.10f}")