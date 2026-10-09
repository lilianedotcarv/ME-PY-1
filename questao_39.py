import random

def adivinhaRapida():
    numero_secreto = random.randint(1, 10)
    palpite = int(input("Adivinhe o número sorteado (entre 1 e 10): "))
    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
    else:
        print(f"Que pena! O número correto era {numero_secreto}.")
