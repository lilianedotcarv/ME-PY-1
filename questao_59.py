def compararNumeros(num1=4, num2=8):
    if num1 % 2 == 0 and num2 % 2 == 0:
        resultado = min(num1, num2)
    else:
        resultado = max(num1, num2)
    print(f"Resultado da comparação entre {num1} e {num2}: {resultado}")
    return resultado
