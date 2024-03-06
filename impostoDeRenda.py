ReceitaBruta = float(input("Insira sua receita bruta anual: "))
dependentes = int(input("Insira o numero de dependetes: "))
TAX_RATE = 0.2
STANDART_DEDUCTION = 10000
DEPENDENT_DEDUCTION = 3000
rendaTributavel = ReceitaBruta - STANDART_DEDUCTION - (DEPENDENT_DEDUCTION * dependentes)
imposto = rendaTributavel * TAX_RATE
print("O imposto de renda é de ", imposto)