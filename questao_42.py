def somaMatriz():
    producao = [
        [10, 20, 30],
        [15, 25, 35],
        [40, 50, 60]
    ]
    soma_total = sum(sum(linha) for linha in producao)
    print(f"Soma de todos os valores da matriz: {soma_total}")
