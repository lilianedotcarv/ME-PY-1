def eNumeroPerfeito(numero):
    if numero <= 0:
        return False
    divisores = [i for i in range(1, numero) if numero % i == 0]
    ePerfeito = sum(divisores) == numero
    print(f"O número {numero} é perfeito? {ePerfeito}")
    return ePerfeito
