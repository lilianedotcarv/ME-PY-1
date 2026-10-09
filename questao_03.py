def producao():
    setor_1 = float(input("Digite a quantidade produzida no Setor 1 (em kg): "))
    setor_2 = float(input("Digite a quantidade produzida no Setor 2 (em kg): "))
    producao_total = setor_1 + setor_2
    print(f"A produção total da cooperativa hoje foi de {producao_total:.2f} kg.")
