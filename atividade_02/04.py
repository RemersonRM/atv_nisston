class ContaBancaria:

    def __init__(self, saldo, titular):
        self.saldo = saldo
        self.titular = titular
    
    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso. Seu saldo é de {self.saldo}")
        else:
            print("Saldo insuficiente.")

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso. Seu saldo é de {self.saldo}")



p1 = ContaBancaria(1500, "Humberto")
valor_do_saque = float(input("Informe o valor do saque: "))
p1.saque(valor_do_saque)
Deposito = float(input("Valor do Deposito: "))
p1.depositar(Deposito)

