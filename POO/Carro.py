class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def acelerar(self, incremento):
        self.velocidade += incremento

    def frear(self, decremento):
        self.velocidade -= decremento
        if self.velocidade < 0:
            self.velocidade = 0

    def status(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Velocidade: {self.velocidade} km/h")


# Exemplo de uso da classe Veiculo
carro1 = Veiculo("Toyota", "Corolla", 2022)
carro1.acelerar(50)
carro1.status()  # Saída: Marca: Toyota, Modelo: Corolla, Ano: 2022, Velocidade: 50 km/h

carro1.frear(20)
carro1.status()  # Saída: Marca: Toyota, Modelo: Corolla, Ano: 2022, Velocidade: 30 km/h
