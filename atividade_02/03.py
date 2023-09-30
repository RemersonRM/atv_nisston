class Retangulo:

    def __init__(self, base, altura) :
        self.base = base
        self.altura = altura
    
    def calcularArea(self):
        Area = self.base * self.altura
        print(Area)
    
p1 = Retangulo(2,4)
p1.calcularArea()