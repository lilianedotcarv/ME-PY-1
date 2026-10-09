def chavesLivro():
    livro = {
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
        "ano": 1899,
        "editora": "Livraria Garnett"
    }
    print("Informações disponíveis no cadastro do livro:")
    for chave in livro.keys():
        print(f"- {chave}")
