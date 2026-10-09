def dividirLucrosTrimestre():
    try:
        lucro = float(input("Digite o lucro total do trimestre: R$ "))
        acionistas = int(input("Digite a quantidade N de acionistas: "))
        divisao = lucro / acionistas
        print(f"Cada acionista receberá: R$ {divisao:.2f}")
    except ZeroDivisionError:
        print("Erro: A quantidade de acionistas não pode ser zero!")
    except ValueError:
        print("Erro: Por favor, informe apenas números válidos para o cálculo.")
