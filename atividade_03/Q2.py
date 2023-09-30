def calcular_fatorial(numero):
    if numero < 0:
        return "Fatorial não está definido para números negativos"
    elif numero == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial

# Solicita ao usuário um número inteiro positivo
numero = int(input("Digite um número inteiro positivo: "))

# Chama a função para calcular o fatorial e imprime o resultado
resultado = calcular_fatorial(numero)
print(f"O fatorial de {numero} é {resultado}")
