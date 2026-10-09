def cadastroFuncionario():
    funcionario = {
        "nome": "João Santos",
        "idade": 30,
        "setor": "Logística"
    }
    print("Dados do funcionário:")
    for chave, valor in funcionario.items():
        print(f"{chave.capitalize()}: {valor}")
