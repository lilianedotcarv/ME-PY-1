from datetime import datetime

while True:

    registro = ()
    print("=====Cadastro de veículo=====")

    try:
        modelo = input("Qual o modelo do veículo? ")

        ano_atual = datetime.now().year
        ano = int(input("Qual o ano do veículo? (ex: 2026): "))
        if ano < 1884 or ano > ano_atual:
            raise Exception("Escreva um ano válido")
           
        km = float(input("Quantos quilometros rodados?: "))
        if km < 0:
            raise Exception("Escreva uma quilometragem válida!")
         
        regitro = modelo, ano, km
        print(f"\nO veículo foi registrado!\nVeículo: {modelo} | Ano: {ano} | KM: {km}\n")

    except ValueError:
        print("Digite apenas números!\n")

    except Exception as erro:
        print(f"Opa! Algo deu errado!\n{erro}\n")

    if modelo == 'sair':
        break
