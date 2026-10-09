def compra():
    valor_compra = float(input("Digite o valor da compra (R$): "))
    if valor_compra >= 500.0:
        print("O cliente tem direito ao desconto promocional!")
    else:
        print("O cliente não atingiu o valor mínimo para o desconto.")
