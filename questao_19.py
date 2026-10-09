import math

def participantesFila():
    n = int(input("Digite o número de participantes (inteiro positivo): "))
    if n >= 0:
        fatorial = math.factorial(n)
        print(f"Existem {fatorial} formas diferentes de organizar a fila.")
    else:
        print("Por favor, digite um número inteiro positivo.")
