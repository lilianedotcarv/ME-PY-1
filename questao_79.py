def cadastrarProduto(nome, preco, quantidade):
    if not isinstance(nome, str) or not nome.strip():
        raise ValueError("O nome do produto não pode ser vazio.")
    if preco <= 0:
        raise ValueError("O preço do produto deve ser maior que zero.")
    if quantidade < 0:
        raise ValueError("A quantidade do produto não pode ser negativa.")
    return f"Sucesso: Produto '{nome.strip()}' cadastrado com sucesso!"
