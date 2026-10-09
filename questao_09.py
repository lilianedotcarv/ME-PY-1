def livroslista():
    livros = []
    for i in range(1, 4):
        titulo = input(f"Digite o título do {i}º livro mais emprestado: ")
        livros.append(titulo)
    print("\nRelatório: Livros Mais Emprestados ")
    for i, livro in enumerate(livros, 1):
        print(f"{i}. {livro}")
