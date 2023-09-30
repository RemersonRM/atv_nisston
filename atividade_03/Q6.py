def contar_vogais(string):
    vogais = "aeiouAEIOU"
    quantidade = 0
    for letra in string:
        if letra in vogais:
            quantidade += 1
    return quantidade

string = input("Digite uma string: ")
quantidade_vogais = contar_vogais(string)
print(f"A quantidade de vogais na string é: {quantidade_vogais}")
