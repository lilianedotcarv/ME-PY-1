def desempenhoTurma():
    alunos = {}
    for i in range(1, 6):
        nome = input(f"Digite o nome do {i}º aluno: ")
        nota = float(input(f"Digite a nota de {nome}: "))
        alunos[nome] = nota
    media_turma = sum(alunos.values()) / len(alunos)
    aprovados = [nome for nome, nota in alunos.items() if nota >= 7.0]
    print(f"\nMédia Geral da Turma: {media_turma:.2f}")
    print("Alunos Aprovados (Nota >= 7.0):", ", ".join(aprovados) if aprovados else "Nenhum")
