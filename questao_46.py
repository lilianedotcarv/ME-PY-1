def somaDiagonal():
    matriz = [
        [10, 2, 3],
        [4, 20, 6],
        [7, 8, 30]
    ]
    soma = sum(matriz[i][i] for i in range(len(matriz)))
    print(f"Soma dos elementos da diagonal principal: {soma}")
