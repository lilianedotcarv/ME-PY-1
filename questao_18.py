def faturamentoSemana():
    faturamento_total = 0.0
    for dia in range(1, 8):
        venda = float(input(f"Digite o valor das vendas do dia {dia}: R$ "))
        faturamento_total += venda
    print(f"Faturamento total da semana: R$ {faturamento_total:.2f}")
