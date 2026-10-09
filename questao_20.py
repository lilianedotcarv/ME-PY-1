def pesquisa():
    soma_notas = 0.0
    while True:
        nota = float(input("Digite uma nota (ou 0 para encerrar): "))
        if nota == 0:
            break
        soma_notas += nota
    print(f"Soma total das notas: {soma_notas}")
