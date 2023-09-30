total = 0
for i in range(5):
    nota = float(input("Digite a sua nota: "))
    total += nota

media = total/5
if media <7:
    print("O aluno foi reprovado com uma media inferior a 7!")
else:
    print("O aluno foi aprovado com uma media superior a 7!")
print(f'A media do aluno foi: ', media)