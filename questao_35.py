def cadastrarProdutos():
    estoque = {}
    for i in range(1, 4):
        produto = input(f"Digite o nome do {i}º produto: ")
        quantidade = int(input(f"Digite a quantidade de {produto}: "))
        estoque[produto] = quantidade
    print("\nProdutos e quantidades cadastradas:")
    for prod, qtd in estoque.items():
        print(f"{prod}: {qtd} unidades")
