def menorCustoMatriz():
    custos = [
        [150.0, 230.5, 99.0],
        [450.0, 88.5, 120.0],
        [310.0, 75.0, 200.0]
    ]
    menor = min(min(linha) for linha in custos)
    print(f"O menor custo registrado é: R$ {menor:.2f}")
