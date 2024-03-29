# Uma companhia monta r´adios cujas pe¸cas s˜ao
# produzidas em trˆes de suas f´abricas denominadas A1, A2 e A3. Elas produzem, respectivamente, 15%, 35% e 50% do total. As probabilides das f´abricas A1, A2 e A3 produzirem
# pe¸cas defeituosas s˜ao 1%; 5% e 2%, respectivamente. Uma pe¸ca ´e escolhida ao acaso do conjunto das pe¸cas produzidas. Essa pe¸ca ´e testada
# e verifica-se que ´e defeituosa. Qual ´e a probabilidade que tenha sido produzida pela f´abrica Ai
# ,
# para i = 1, 2, 3?
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
        producao = coeficiente(fabrica)    # Verifica qual fábrica foi produzido
        if producao:
            if coeficiente(defeito):    # Verifica se houve defeito
                cont += 1
    return cont / ciclo


# definindo variável de repetição
ciclo = 10**6

# Chamando as funções
defeito_fabrica_a = defeito(ciclo, prod_a, defeito_a)   # 15000
defeito_fabrica_b = defeito(ciclo, prod_b, defeito_b)   # 175000
defeito_fabrica_c = defeito(ciclo, prod_c, defeito_c)   # 100000


# Calculando a probabilidade de defeito por fábrica fazendo a quantidade de defeito de cada dividido pelo numero total de defeito somado de todas as fábricas
probabilidade_defeito_fabrica_a = defeito_fabrica_a / (defeito_fabrica_a + defeito_fabrica_b + defeito_fabrica_c)
probabilidade_defeito_fabrica_b = defeito_fabrica_b / (defeito_fabrica_a + defeito_fabrica_b + defeito_fabrica_c)
probabilidade_defeito_fabrica_c = defeito_fabrica_c / (defeito_fabrica_a + defeito_fabrica_b + defeito_fabrica_c)
print(f"A probabilidade da peças defeituosa ser da fabrica A é de {probabilidade_defeito_fabrica_a*100:.2f}%")
print(f"A probabilidade da peças defeituosa ser da fabrica B é de {probabilidade_defeito_fabrica_b*100:.2f}%")
print(f"A probabilidade da peças defeituosa ser da fabrica C é de {probabilidade_defeito_fabrica_c*100:.2f}%")
