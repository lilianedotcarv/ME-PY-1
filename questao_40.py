import random

def adivinhaDicas():
    numeroSecreto = random.randint(1, 100)
    tentativas = 0
    print("Tente adivinhar o número entre 1 e 100!")
    while True:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1
        if palpite == numeroSecreto:
            print(f"Parabéns! Você acertou em {tentativas} tentativa(s)!")
            break
        elif palpite < numeroSecreto:
            print("O número procurado é MAIOR.")
        else:
            print("O número procurado é MENOR.")
