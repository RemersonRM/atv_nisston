class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f'Meu nome é {self.nome}, e tenho {self.idade} anos')

p1 = Pessoa("humberto", 18)
p1.falar()