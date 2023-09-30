class temperatura:

    def __init__(self):
        self.fahrenheit = 0.0
        self.celcius = 0.0
    
    def Cf(self):
        self.fahrenheit = float(input("Qual a temperatura em fahrenheit: "))
        self.celcius = (self.fahrenheit - 32) * 5/9
        print(f'A temperatura {self.fahrenheit}, equivale a {self.celcius}')
    
    def fc (self):
        self.celcius = float(input("Informe a temperatura em celcius: "))
        self.fahrenheit = (self.celcius * 9/5) + 32
        print(f'A temperatura {self.celcius}, equivale a {self.fahrenheit}')

t1 = temperatura()
t1.fc()


