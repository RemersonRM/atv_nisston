class Produto:

    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_preco(self):
        total = self.preco * self.quantidade
        print(f'A sua compra resultou um total de {total}')

p1 = Produto("abacaxi", 10, 15)
p1.calcular_preco()