def aplicarDescontoPrecos(listaPrecosStr):
    precosComDesconto = []
    for item in listaPrecosStr:
        try:
            preco = float(item)
        except ValueError:
            print(f"Falha ao converter '{item}' para número.")
        else:
            precoDesconto = preco * 0.90
            precosComDesconto.append(precoDesconto)
            print(f"Preço R$ {preco:.2f} com 10% de desconto -> R$ {precoDesconto:.2f}")
    return precosComDesconto
