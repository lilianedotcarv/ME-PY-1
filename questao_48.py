def matrizIdentidade():
    ordem = 3
    matriz = [[1 if i == j else 0 for j in range(ordem)] for i in range(ordem)]
    print("Matriz Identidade 3x3:")
    for linha in matriz:
        print(linha)
