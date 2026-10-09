def receberNumeros():
    numeros = []
    print("Digite 5 números reais:")
    for i in range(1, 6):
        num = float(input(f"Digite o {i}º número: "))
        numeros.append(num)
    return numeros

def encontrarMaior(numeros):
    return max(numeros)

def encontrarMenor(numeros):
    return min(numeros)
