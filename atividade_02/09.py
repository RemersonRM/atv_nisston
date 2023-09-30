class Trianguo:

    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def calcular_Perimetro(self):
        P = self.lado1 + self.lado2 + self.lado3
        print(f'O perimetro desse triangulo é de {P}')

t1 = Trianguo(5,8,5)
t1.calcular_Perimetro()