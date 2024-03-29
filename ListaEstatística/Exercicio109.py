# Seja A o evento em que uma carta retirada
# aleatoriamente de um baralho de 52 cartas seja
# vermelha, e B o evento que esta carta ´e uma
# rainha. S˜ao eventos independentes A e B? O
# que acontece se o evento B ´e o evento que a
# carta retirada seja rainha de copas?
import random as rn


# Função para determinar a probabilidade de acontecer o evento "escolher carta vermelha"
def evento_a(ciclo):    # Sair carta vermelha
    vezes_numero_aparece = 0    # Contador quando condição é satisfeita
    cartas = ["pretas", "vermelhas"]    # Lista com duas cartas possíveis
    for i in range(ciclo):
        resultado = rn.choice(cartas)
        if resultado == "vermelhas":
            vezes_numero_aparece += 1
    return vezes_numero_aparece / ciclo


# Função para determinar a probabilidade de acontecer o evento "escolher uma rainha"
def evento_b(ciclo):    # Sair carta rainha
    vezes_numero_aparece = 0    # Contador quando condição é satisfeita
    cartas_baralho = 52     # Número total de cartas em um baralho
    cartas_naipe = 4    # Número de cartas por naipe
    const_rainha = 12
    for i in range(ciclo):
        resultado = rn.randint(1, cartas_baralho // cartas_naipe)    # Número aleatório de 1 a 13
        if resultado == const_rainha:
            vezes_numero_aparece += 1
    return vezes_numero_aparece / ciclo


# Função para calcular a probabilidade de ser rainha de copas
def novo_evento_b(ciclo):
    vezes_numero_aparece = 0
    cartas_baralho = 52
    cartas_naipe = 4
    const_rainha = 12
    for i in range(ciclo):
        resultado = rn.randint(1, cartas_baralho // cartas_naipe)
        if resultado == const_rainha:
            lista = ["copas", "ouro", "paus", "espada"]
            resultado = rn.choice(lista)
            if resultado == "copas":
                vezes_numero_aparece += 1
    return vezes_numero_aparece / ciclo


ciclo = 10**6

# chamando funções
print(f"A probabiliade de sair carta vermelha (evento A) é de {evento_a(ciclo)*100:.2f}%")
print(f"A probabiliade de sair carta rainha (evento B)é de {evento_b(ciclo)*100:.2f}%")
print("São eventos independentes, pois pra sair carta vermelha não necessariamente precisa ser uma rainha,\ne pra sair uma rainha não necessariamente precisa ser vermelha")
print(f"A probabiliade de sair rainha de copas é de {novo_evento_b(ciclo)*100:.2f}%")
print("Neste casa os dois eventos deixam de ser independentes, pois para o evento B ocorrer o evento A precisa ocorrer")
