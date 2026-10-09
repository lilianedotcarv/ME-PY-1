def codigoLista():
    codigos = [101, 102, 103, 104, 105]
    codigobusca = int(input("Digite o código do produto a ser pesquisado: "))
    if codigobusca in codigos:
        print(f"O código {codigobusca} está presente no sistema.")
    else:
        print(f"O código {codigobusca} NÃO foi encontrado.")
