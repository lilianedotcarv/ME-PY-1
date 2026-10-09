def equipamento():
    codigo = int(input("Digite o código do equipamento: "))
    if codigo % 2 == 0:
        print(f"O equipamento {codigo} é PAR (Setor Administrativo).")
    else:
        print(f"O equipamento {codigo} é ÍMPAR (Setor Operacional).")
