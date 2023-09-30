def filtrar_nomes_iniciados_com_a(lista_nomes):
    nomes_com_a = [nome for nome in lista_nomes if nome.startswith('A') or nome.startswith('a')]
    return nomes_com_a

# Lê a lista de nomes do usuário
entrada = input("Digite a lista de nomes separados por espaços: ")
nomes = entrada.split()

nomes_iniciados_com_a = filtrar_nomes_iniciados_com_a(nomes)

print("Nomes que começam com a letra 'A':", nomes_iniciados_com_a)
