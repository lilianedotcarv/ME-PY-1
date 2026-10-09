def cadastrarIdadeUsuario():
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if idade < 0:
                raise ValueError("A idade não pode ser um número negativo.")
            print(f"Idade {idade} cadastrada com sucesso!")
            return idade
        except ValueError as e:
            print(f"Entrada inválida ({e}). Por favor, tente novamente.\n")
