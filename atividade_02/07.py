class Carro:

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        print(f'A marca do carro é {self.marca}')
        print(f'O modelo do carro é {self.modelo}')
        print(f'O ano do carro é {self.ano}')

c1 = Carro("vw", "sedan", 2005)
c1.detalhes()