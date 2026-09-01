#01
def livros():
    quantidade_livros = int(input("Digite a quantidade de livros lidos pela turma vencedora: "))

    print(f"A turma vencedora leu {quantidade_livros} livros!")
    livros()

#02
def estudante():
    nome = input("Digite o nome completo do estudante: ")

    print(f"Seja bem-vindo(a) à instituição de ensino, {nome}!")
    estudante()

#03
def producao():
    setor_1 = float(input("Digite a quantidade produzida no Setor 1 (em kg): "))
    setor_2 = float(input("Digite a quantidade produzida no Setor 2 (em kg): "))

    producao_total = setor_1 + setor_2

    print(f"A produção total da cooperativa hoje foi de {producao_total:.2f} kg.")
    producao()

#04
def medialuno():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2) / 2

    print(f"A média do estudante é: {media:.2f}")
    medialuno()

#05
def compra():
    valor_compra = float(input("Digite o valor da compra (R$): "))

    if valor_compra >= 500.0:
        print("O cliente tem direito ao desconto promocional!")
    else:
        print("O cliente não atingiu o valor mínimo para o desconto.")
    compra()
#06
def equipamento():
    codigo = int(input("Digite o código do equipamento: "))


    if codigo % 2 == 0:
        print(f"O equipamento {codigo} é PAR (Setor Administrativo).")
    else:
        print(f"O equipamento {codigo} é ÍMPAR (Setor Operacional).")
    equipamento()

#07
def onibus():
    print("Lista de Assentos do Ônibus")
    for assento in range(1, 21):
        print(f"Assento número: {assento}")
    onibus()

#08
def alimentos():
    alimentos = 0.0

    for i in range(1, 6):
        quantidade = float(input(f"Digite a quantidade de alimentos arrecadada pelo voluntário {i} (em kg): "))
        total_alimentos += quantidade

    print(f"\nO total de alimentos arrecadados na campanha foi: {alimentos:.2f} kg")
    alimentos()

#09
def livroslista():
    livros = []

    for i in range(1, 4):
        titulo = input(f"Digite o título do {i}º livro mais emprestado: ")
        livros.append(titulo)

    print("\nRelatório: Livros Mais Emprestados ")
    for i, livro in enumerate(livros, 1):
        print(f"{i}. {livro}")
    livroslista()

#10
def semana():
    dias_da_semana = ("Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo")

    print(f"O primeiro dia da semana na escala é: {dias_da_semana[0]}")
    semana()

#12
def limite():
#17
    limite= 80.0

    velocidade = float(input("Digite a velocidade registrada do veículo (km/h): "))


    if velocidade > limite:
        print(f"ALERTA: Velocidade de {velocidade:.1f} km/h ultrapassou o limite permitido de 80 km/h!")
    else:
        print(f"Velocidade de {velocidade:.1f} km/h dentro do limite permitido.")
    limite()

#13
def setor_consumo():
    consumo_setor1 = float(input("Digite o consumo de energia do Setor 1 (kWh): "))
    consumo_setor2 = float(input("Digite o consumo de energia do Setor 2 (kWh): "))


    if consumo_setor1 > consumo_setor2:
        print(f"O Setor 1 apresentou o MAIOR consumo: {consumo_setor1:.2f} kWh.")
    elif consumo_setor2 > consumo_setor1:
        print(f"O Setor 2 apresentou o MAIOR consumo: {consumo_setor2:.2f} kWh.")
    else:
        print(f"Consumiram igual!")
    setor_consumo()
    
        
#17
def cestas():
    cestas = 0 

    for segundo in range(10, 0, -1):
        qnt = int(input(f"Digite quantas cestas foram arrecadadas{i}:"))
        total += qnt
        
    print(f"Total de cestas arrecadadas:{total}")

    print(f"Ambos os setores registraram o mesmo consumo: {consumo_setor1:.2f} kWh.")
    cestas()

#14
def visitantes():
    range(1, 51)
    print(" Controle de Visitantes da Feira de Ciências")
    for visitante in range(1, 51):
        print(f"Visitante nº {visitante}")
    visitantes()

#15 
def ex():
    print("sequencia de exercicios")
    for exercicio in range(1, 16):
        print(f"Exercicio: {exercicio}")
    ex()

#16
def contagem():
    print("Iniciando Contagem")
    for segundo in range(10, 0, -1):
        print(segundo)
        
    print("lançamento!")
    contagem()

#17
def cestas():
    cestas = 0 

    for segundo in range(10, 0, -1):
        qnt = int(input(f"Digite quantas cestas foram arrecadadas{i}:"))
        total += qnt
        
    print(f"Total de cestas arrecadadas:{total}")
    cestas()

#18

