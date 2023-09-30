def selecao_Ordem(vetor, ordem):
    n = len(vetor)
    if ordem ==0:
        for i in range(n):  
            indiceM = i
            for j in range(i + 1, n):
                if vetor[j] < vetor[indiceM]:
                    indiceM = j
            vetor[i], vetor[indiceM] = vetor[indiceM], vetor[i]
    else:
        for i in range(n):
            indiceM = i
            for j in range(i + 1, n):
                if vetor[j] > vetor[indiceM]:
                    indiceM = j
            vetor[i], vetor[indiceM] = vetor[indiceM], vetor[i]
    #crirar uma variavel para que leia a quantidade de elementos que tenham dentro do vetor

vetor = [5, 4, 7, 0, 1, 2, 8, 9, 10, 3, 6]
#criar um vetor com numeros de maneira desordenadas-
selecao_Ordem(vetor,0)
#atribuindo a opçã de ordem crescente derivada da condição dada pelo if
print(vetor)
selecao_Ordem(vetor,1)
#atribuindo a opçã de ordem decrescente derivada da condição dada pelo if

print(vetor)