

def selecao_Ordem(vetor):
    n = len(Vetor)
    #crirar uma variavel para que leia a quantidade de elementos que tenham dentro do vetor

    for i in range(n):  
        indiceM = i
        for j in range(i + 1, n):
            if vetor[j] < vetor[indiceM]:
                indiceM = j
        vetor[i], vetor[indiceM] = vetor[indiceM], vetor[i]


Vetor = [5, 4, 7, 0, 1, 2, 8, 9, 10, 3, 6]
#criar um vetor com numeros de maneira desordenadas-
selecao_Ordem(Vetor)
print(Vetor)
