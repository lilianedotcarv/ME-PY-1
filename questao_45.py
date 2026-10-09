def diagonalPrincipal():
    matriz = [
        [5, 2, 9],
        [1, 7, 3],
        [8, 4, 6]
    ]
    elementos_diagonal = [matriz[i][i] for i in range(len(matriz))]
    print("Elementos da diagonal principal:", elementos_diagonal)
