class calcularIndice:

    def __init__(self):
        self.nome = ' '
        self.altura = 0.0
        self.peso = 0.0
    
    def calcular(self):
        self.nome = str(input("Digite seu nome: "))
        self.peso = float(input("Digite o seu peso: "))
        self.altura = float(input("informe a sua altura: "))
        IMC = self.peso/(self.altura ** 2 )
        print(f'Seja bem-vindo {self.nome}O IMC é de {IMC:.2f}')


c1 = calcularIndice()
c1.calcular()