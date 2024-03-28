import random as rn

def taxa_erro(taxa):
    rando = rn.random()
    if rando < taxa:
        return True
    else:
        return False

def cometer_erro(ciclo):
    cont = 0
    for i in range(ciclo):
        for j in range(4):
            erro = taxa_erro(0.1)
            if erro:
                cont += 1
                break
    return cont / ciclo

ciclo = 10**6
print(f"Probabilidade de uma pessoa de 4 cometer erro {cometer_erro(ciclo)*100:.2f}%")