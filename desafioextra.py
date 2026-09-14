try:
    arquivo_vendas = open("vendas.txt", "a", encoding="utf-8")
    log_erros = open("log_erros.txt", "a", encoding="utf-8")

    produto = input("Nome do produto?")
    quantidade = int(input("Quantidade so produto?"))
    valor = float(input("Preço?"))

    if not produto:
        raise ValueError("O produto não pode ficar vazio.")

    if quantidade <= 0:
        raise ValueError("A quantidade deve ser maior que 0.")

    if valor <= 0:
        raise ValueError("O preço deve ser maior que 0.")


    lucro = quantidade * valor

    arquivo_vendas.write(
        f"Produto: {produto} | "
        f"Quantidade: {quantidade} | "
        f"Preço: R$ {valor:.2f} | "
        f"Lucro: R$ {lucro:.2f}\n"
    )

    print("Venda registrada com sucesso!")

    arquivo_vendas.close()

except ValueError as erro:
    with open("log_erros.txt", "a", encoding="utf-8") as log:
        log.write(f"Erro {ValueError}")

