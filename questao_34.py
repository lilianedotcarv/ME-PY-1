def consultarNota():
    notas = {
        "Ana": 8.5,
        "Bruno": 7.0,
        "Carla": 9.2,
        "Daniel": 6.5
    }
    nome = input("Digite o nome do estudante para consultar a nota: ")
    if nome in notas:
        print(f"A nota de {nome} é: {notas[nome]}")
    else:
        print("Estudante não encontrado no sistema.")
