

class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        self.raio = float(self.raio **2)
        return self.raio

# Exemplo de uso
raio_do_circulo = 5
circulo = Circulo(raio_do_circulo)
area = circulo.calcular_area()
print(f"A área do círculo com raio {raio_do_circulo} é: {area:.2f}")
