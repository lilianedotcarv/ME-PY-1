def alimentos():
    total_alimentos = 0.0
    for i in range(1, 6):
        quantidade = float(input(f"Digite a quantidade de alimentos arrecadada pelo voluntário {i} (em kg): "))
        total_alimentos += quantidade
    print(f"\nO total de alimentos arrecadados na campanha foi: {total_alimentos:.2f} kg")
