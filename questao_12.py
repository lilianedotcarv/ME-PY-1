def limite():
    limite = 80.0
    velocidade = float(input("Digite a velocidade registrada do veículo (km/h): "))
    if velocidade > limite:
        print(f"ALERTA: Velocidade de {velocidade:.1f} km/h ultrapassou o limite permitido de 80 km/h!")
    else:
        print(f"Velocidade de {velocidade:.1f} km/h dentro do limite permitido.")
