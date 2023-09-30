#SISTEMA DE IMPRESTIMO BANCARIO USANDO POO

class Conta:

    def __init__(self):
        self.nome = ' '
        self.conta = ' '
        self.saldo = 0.0

    def abrir_Conta(self):
        self.nome = str(input("Digite seu nome: "))
        self.conta = str(input("Digite o numero da sua conta: "))

    def depositar(self, valor):
        self.saldo += valor
        print(f'Deposito feito no valor de {valor:.2f}, seu saldo atual é de {self.saldo}')

    def Saque(self, valor):
        self.saldo -= valor

    def status(self):
        print(f'nome {self.nome}, numero da conta {self.conta}')
        print(f'Seu saldo atual é de: {self.saldo:.2f}', )


c1 = Conta()
c1.abrir_Conta()
Deposito = float(input("Valor do deposito: "))
valor_Saque = float(input("Qual o valor do saque: "))
c1.depositar(Deposito)
c1.Saque(valor_Saque)
c1.status()
