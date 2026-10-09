def somaAjustada(a, b, c):
    soma = a + b + c
    if soma <= 21:
        return soma
    if soma > 21 and (a == 11 or b == 11 or c == 11):
        soma -= 10
    if soma > 21:
        return -1
    return soma
