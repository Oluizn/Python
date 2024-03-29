# Se a probabilidade de que uma pessoa cometa
# um erro em sua declara¸c˜ao de imposto de renda
# ´e de 0,1; determine a probabilidade de que:
# a.) uma de quatro pessoas, que n˜ao tˆem nenhuma rela¸c˜ao entre si, cometa um erro.
# b.) que Jo˜ao e Alberto cometam um erro e
# Roberto e M´arcia n˜ao cometam erro.
import random as rn


# Função para o coeficiente
def taxa_erro(taxa):
    rando = rn.random()
    if rando < taxa:
        return True
    else:
        return False


# Função para que uma em quatro pessoas cometam um erro
def cometer_erro(ciclo):
    cont = 0
    const_pessoas = 4
    for i in range(ciclo):
        for j in range(const_pessoas):
            erro = taxa_erro(0.1)
            if erro:
                cont += 1
                break
    return cont / ciclo


# Função para que duas em quatro pessoas cometam um erro
def cometer_erro_dois(ciclo):
    cont_geral = 0
    pessoas = 4
    for i in range(ciclo):
        cont = 0
        for j in range(pessoas):
            erro = taxa_erro(0.1)
            if erro:
                cont += 1
        if cont == 2:
            cont_geral += 1
    return cont_geral / ciclo


ciclo = 10**6

print(f"Probabilidade de 1 em 4 pessoas cometer erro {cometer_erro(ciclo)*100:.2f}%")
print(f"Probabilidade de 2 em 4 pessoas cometer erro {cometer_erro_dois(ciclo)*100:.2f}%")
