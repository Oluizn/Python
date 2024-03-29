# Suponhamos uma urna contendo bolas idˆenticas
# sendo: 4 azuis, 5 vermelhas e 2 roxas. S˜ao extra´ıdas 2 bolas sem reposi¸c˜ao. Calcule a probabilidade de:
# a.) ser extra´ıda ao menos 1 bola roxa;
# b.) as duas bolas serem da mesma cor.
# c.) a segunda bola ser roxa, dado que a primeira
# foi vermelha.
import random as rn

bolas_azuis = 4
bolas_vermelhas = 5
bolas_roxas = 2
total_bolas = bolas_azuis + bolas_roxas + bolas_vermelhas


# Função para gerar um número aleatório entre 0 e 1
def taxa_escolha(taxa):
    rando = rn.random()
    if rando < taxa:
        return True
    else:
        return False


# Função para ver quantas bolas roxas são escolhidas
def prob_bola_roxa(ciclo):
    cont = 0

    # Variáveis locais recebem valor das variáveis globais
    roxa = bolas_roxas
    total = total_bolas
    const_bolas = 2
    for i in range(ciclo):

        # Retirada de duas bolas sem reposição
        for j in range(const_bolas):
            escolha = taxa_escolha(roxa / total)
            if escolha:
                cont += 1
                # Subtrai uma bola roxa, reduzindo a quantidade de roxas e do total para a equação
                roxa -= 1
                total -= 1
                break
            else:
                # Subtrai apenas uma bola do total de bolas sem ser a roxa
                total -= 1

        # Retorna o valor global para as variáveis locais para próxima tentativa
        roxa = bolas_roxas
        total = total_bolas

    return cont / ciclo


# Função para verificar a probabilidade de vir duas bolas roxas
def prob_2_roxa(ciclo):
    # Variáveis locais recebem valor das variáveis globais
    total = total_bolas
    roxa = bolas_roxas
    cont = 0
    cont_geral = 0
    const_bolas = 2
    for i in range(ciclo):
        for j in range(const_bolas):
            resultado = taxa_escolha(roxa / total)
            if resultado:
                cont += 1       # Contador até 2 para verificar se vão ser duas bolas iguais
                roxa -= 1
                total -= 1
            else:
                cont = 0
                break
        if cont == const_bolas:
            cont_geral += 1     # Contador de acertos com duas bolas iguais
        roxa = bolas_roxas
        total = total_bolas
    return cont_geral / ciclo


# Função para verificar a probabilidade de vir duas bolas vermelhas
def prob_2_vermelha(ciclo):
    # Variáveis locais recebem valor das variáveis globais
    total = total_bolas
    vermelha = bolas_vermelhas
    cont = 0
    cont_geral = 0
    const_bolas = 2
    for i in range(ciclo):
        for j in range(const_bolas):
            resultado = taxa_escolha(vermelha / total)
            if resultado:
                cont += 1       # Contador até 2 para verificar se vão ser duas bolas iguais
                vermelha -= 1
                total -= 1
            else:
                cont = 0
                break
        if cont == const_bolas:
            cont_geral += 1     # Contador de acertos com duas bolas iguais
        vermelha = bolas_vermelhas
        total = total_bolas
    return cont_geral / ciclo


# Função para verificar a probabilidade de vir duas bolas azuis
def prob_2_azul(ciclo):
    # Variáveis locais recebem valor das variáveis globais
    total = total_bolas
    azul = bolas_azuis
    cont = 0
    cont_geral = 0
    const_bolas = 2
    for i in range(ciclo):
        for j in range(const_bolas):
            resultado = taxa_escolha(azul / total)
            if resultado:
                cont += 1       # Contador até 2 para verificar se vão ser duas bolas iguais
                azul -= 1
                total -= 1
            else:
                cont = 0
                break
        if cont == const_bolas:
            cont_geral += 1     # Contador de acertos com duas bolas iguais
        azul = bolas_azuis
        total = total_bolas
    return cont_geral / ciclo


# Função para verificar a probabilidade de vir uma vermelha e depois uma roxa
def vermelha_then_roxa(ciclo):
    vermelha = bolas_vermelhas
    roxa = bolas_roxas
    total = total_bolas
    cont = 0
    for i in range(ciclo):
        primeira = taxa_escolha(vermelha / total)
        if primeira:
            total -= 1
            segunda = taxa_escolha(roxa / total)
            if segunda:
                cont += 1
        total = total_bolas
    return cont / ciclo


ciclo = 10**6

print(f"A probabilidade da bola roxa ser escolhida é de {prob_bola_roxa(ciclo)*100:.2f}%")
print(f"A probabilidade das bolas serem das mesma cor {(prob_2_azul(ciclo)*100)+(prob_2_vermelha(ciclo)*100)+(prob_2_roxa(ciclo)*100):.2f}%")
print(f"A probabilidade da segunda bola ser roxa, dada que a primeira foi vermelha, é de {vermelha_then_roxa(ciclo)*100:.2f}%")
