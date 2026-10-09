def cestasArrecadadas():
    total_cestas = 0
    for i in range(1, 11):
        qnt = int(input(f"Digite quantas cestas foram arrecadadas pelo voluntário {i}: "))
        total_cestas += qnt
    print(f"Total de cestas arrecadadas: {total_cestas}")
