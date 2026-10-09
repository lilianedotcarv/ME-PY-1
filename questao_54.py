def ocupacaoEstacionamento():
    estacionamento = [
        [1, 0, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]
    ocupadas = sum(linha.count(1) for linha in estacionamento)
    livres = sum(linha.count(0) for linha in estacionamento)
    print(f"Vagas Ocupadas: {ocupadas}")
    print(f"Vagas Livres: {livres}")
