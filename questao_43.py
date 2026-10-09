def maiorValorMatriz():
    dados = [
        [12, 45, 23],
        [67, 89, 34],
        [54, 11, 78]
    ]
    maior = max(max(linha) for linha in dados)
    print(f"O maior valor na matriz é: {maior}")
