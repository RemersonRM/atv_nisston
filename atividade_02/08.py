class Aluno:

    def __init__(self, nome, nota1, nota2, nota3) -> None:
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def Calcular_Media(self):
        media = (self.nota1 + self.nota2 + self.nota3)/3
        if media >=7:
            print(f'A media do aluno {self.nome}, é de {media}')
        else:
            print(f'O aluno {self.nome}, reprovou com a media de {media}')
            

A1 = Aluno("humberto", 8, 9, 5)
A1.Calcular_Media()