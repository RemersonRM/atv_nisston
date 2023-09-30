def calcular_fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

# Solicita o número inteiro positivo ao usuário
numero = int(input("Digite um número inteiro positivo: "))

if numero < 0:
    print("O número deve ser positivo.")
else:
    fatorial = calcular_fatorial(numero)
    print(f"O fatorial de {numero} é {fatorial}")
