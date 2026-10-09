def cadastrarAlunos():
    alunos = {}
    for i in range(1, 6):
        nome = input(f"Digite o nome do {i}º aluno: ")
        nota = float(input(f"Digite a nota de {nome}: "))
        alunos[nome] = nota
    print("\nRegistros de Alunos:")
    for nome, nota in alunos.items():
        print(f"Aluno: {nome} | Nota: {nota:.1f}")
