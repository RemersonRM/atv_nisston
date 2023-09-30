import numpy as np
class ListaSequencial:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype = int)

    def imprime(self):
        if self.ultima_posicao == -1:
            print('o valor esta vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])
    
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade -1:
            print('Capacidade maxima atiginda')

        else:
            self.ultima_posicao +=1
            self.valores[self.ultima_posicao] = valor

    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if(valor == self.valores[i]):
                if(valor == self.valores[i]):
                    return i
        return -1
    
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
        self.ultima_posicao -= 1

p1 = ListaSequencial(5)

p1.insere(4)
p1.insere(3)
p1.insere(5)
p1.excluir(5)
print('===========')
p1.pesquisar(4)
p1.imprime()