import random

def indicarLivro():
    livros = ["1984", "O Hobbit", "O Pequeno Príncipe", "Capitães da Areia", "A Hora da Estrela"]
    livroSorteado = random.choice(livros)
    print(f"Sugestão de leitura de hoje: '{livroSorteado}'")
