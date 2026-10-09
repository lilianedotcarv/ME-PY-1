def controleFarmacia():
    estoque = {}
    print("--- Cadastro de Medicamentos ---")
    for i in range(1, 6):
        med = input(f"Digite o nome do {i}º medicamento: ").strip().capitalize()
        qtd = int(input(f"Digite a quantidade de {med} em estoque: "))
        estoque[med] = qtd
    print("\n--- Consulta de Estoque ---")
    busca = input("Digite o nome do medicamento para consultar: ").strip().capitalize()
    if busca in estoque:
        print(f"Estoque de {busca}: {estoque[busca]} unidade(s).")
    else:
        print("Medicamento não cadastrado no sistema.")
