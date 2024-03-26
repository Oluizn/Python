import random as rn
def TaxaSucesso(taxa):
    rando = rn.random()
    #print("E", rando)
    if rando < taxa:
        return True
    else:
        return False

def Slide21_Ex4():
    #valores fixos
    ProbEngravidar = 0.2
    NumeroTentativas = 4

    #valores variáveis
    NumeroRepeticoes = 100000000000000000000
    NumeroSucessos = 0
    NumeroMeses = 0

    for i in range(int(NumeroRepeticoes)):
        while True:
            NumeroMeses += 1
            Gravida = TaxaSucesso(ProbEngravidar)

            if Gravida:
                if NumeroMeses >= 4:
                    NumeroSucessos += 4
                    break

    ProbabilidadeGravidez = NumeroSucessos/NumeroRepeticoes
    print(f"Probabilidade de engravidar no mes {NumeroTentativas}: {ProbabilidadeGravidez}")