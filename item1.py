veiculos = {}

print("=====Cadastro de veículo=====")

while True:
    modelo_veiculo = input("Qual o modelo do veículo? ")
        
    if modelo_veiculo.lower() == 'sair':
        break

    try:
        ano_veiculo = int(input("Qual o ano do veículo? (ex: 2026): "))
        if ano_veiculo < 1884:
            raise Exception("Escreva um numero maior que 1884!")
            
        km_rodados = float(input("Quantos quilometros rodados?: "))
        if km_rodados < 0:
            raise Exception("Escreva uma quilometragem válida!")
         
        veiculos[modelo_veiculo] = [ano_veiculo, km_rodados]

        print(f"\nO veículo foi registrado!\nVeículo: {modelo_veiculo} | Ano: {ano_veiculo} | KM: {km_rodados}\n")

    except ValueError:
        print("Digite apenas números!\n")

    except Exception as erro:
        print(f"Opa! Algo deu errado!\n{erro}\n")

print("\n--- Lista de Veículos Cadastrados ---")
for veiculo, valor in veiculos.items():
    print(f"Veículo: {veiculo} | Ano: {valor[0]} | KM: {valor[1]}")