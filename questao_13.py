def setor_consumo():
    consumo_setor1 = float(input("Digite o consumo de energia do Setor 1 (kWh): "))
    consumo_setor2 = float(input("Digite o consumo de energia do Setor 2 (kWh): "))
    if consumo_setor1 > consumo_setor2:
        print(f"O Setor 1 apresentou o MAIOR consumo: {consumo_setor1:.2f} kWh.")
    elif consumo_setor2 > consumo_setor1:
        print(f"O Setor 2 apresentou o MAIOR consumo: {consumo_setor2:.2f} kWh.")
    else:
        print("Ambos os setores apresentaram consumo igual!")
