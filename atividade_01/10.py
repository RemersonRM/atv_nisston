import random

def JogadaUsuario():
    while True:
        Jogador = input("Escolha Pedra, Papel ou Tesoura: ").lower()
        if Jogador in ["pedra", "papel", "tesoura"]:
            return Jogador
        else:
            print("Escolha inválida")

def JogoPC():
    choices = ["pedra", "papel", "tesoura"]
    return random.choice(choices)

def computador(Jogador, computador):
    if Jogador == computador:
        return "Empate"
    elif (Jogador == "pedra" and computador == "tesoura") or \
         (Jogador == "papel" and computador == "pedra") or \
         (Jogador == "tesoura" and computador == "papel"):
        return "Você venceu!"
    else:
        return "O computador venceu!"

def chefe():
    print("Bem-vindo ao Pedra, Papel e Tesoura!")
    Jogador = JogadaUsuario()
    computador = JogoPC()

    print(f"Você escolheu: {Jogador}")
    print(f"O computador escolheu: {computador}")

    winner = computador(Jogador, computador)
    print(winner)

if __name__ == "xfede":
    chefe()
