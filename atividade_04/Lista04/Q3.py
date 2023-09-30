def encontrar_Max(vetor):
    maximo = vetor[0]

    for elemeneto in vetor:
    
        if elemeneto > maximo:
            maximo = elemeneto
    return maximo

def encontrar_Min(vetor):
    minimo = vetor[0]
    
    for elemeneto in vetor:
        if elemeneto < minimo:
            minimo = elemeneto
    return minimo

def encontrar_max_Min(vetor):
    maximo = vetor[0]
    minimo = vetor[0]
    
    for elemeneto in vetor:
        if elemeneto > maximo:
            maximo = elemeneto
        if elemeneto < minimo:
            minimo = elemeneto
    return maximo, minimo

vetor = [1 ,3,5,6,8,7,6,5,4]
#print(encontrar_Max(vetor))
#print(encontrar_Min(vetor))
rep = encontrar_max_Min(vetor)
print(rep[0], rep[1])
