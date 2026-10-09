def monitorEstufa():
    temperaturas = []
    for dia in range(1, 6):
        temp = float(input(f"Digite a temperatura média do {dia}º dia (°C): "))
        temperaturas.append(temp)
    media_temp = sum(temperaturas) / len(temperaturas)
    print("\n--- Relatório de Temperaturas ---")
    print(f"Temperaturas registradas: {temperaturas}")
    print(f"Média das temperaturas: {media_temp:.1f}°C")
    if 18.0 <= media_temp <= 28.0:
        print("Status: A média ESTÁ dentro da faixa ideal de cultivo (18°C a 28°C).")
    else:
        print("Status: ALERTA! A média está FORA da faixa ideal de cultivo.")
