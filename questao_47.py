def contarPositivos():
    matriz = [
        [-5, 10, -3],
        [8, -2, 15],
        [0, 7, -1]
    ]
    positivos = sum(1 for linha in matriz for val in linha if val > 0)
    print(f"Quantidade de valores positivos: {positivos}")
