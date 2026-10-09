def desempenhoEscolar():
    disciplinas = ("Matemática", "Português")
    turma = {}
    qtd_alunos = int(input("Digite a quantidade de alunos a cadastrar: "))
    for i in range(qtd_alunos):
        nome = input(f"\nDigite o nome do {i+1}º aluno: ")
        nota_mat = float(input(f"Nota em {disciplinas[0]}: "))
        nota_port = float(input(f"Nota em {disciplinas[1]}: "))
        turma[nome] = {
            disciplinas[0]: nota_mat,
            disciplinas[1]: nota_port
        }
    print("\n--- RESULTADOS FINAIS ---")
    print(f"Disciplinas avaliadas: {disciplinas[0]} e {disciplinas[1]}\n")
    for aluno, notas in turma.items():
        media = (notas[disciplinas[0]] + notas[disciplinas[1]]) / 2
        situacao = "Aprovado" if media >= 7.0 else "Reprovado"
        print(f"Aluno: {aluno} | Média: {media:.2f} | Situação: {situacao}")
