import math
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
def cestasArrecadadas():
    total_cestas = 0
    for i in range(1, 11):
        qnt = int(input(f"Digite quantas cestas foram arrecadadas{i}:"))
        total += qnt
        
    print(f"Total de cestas arrecadadas:{total}")
cestasArrecadadas()

#18
def faturamentoSemana():
    faturamento_total = 0.0

    for dia in range(1, 8):
        venda = float(input(f"Digite o valor das vendas do dia {dia}: R$ "))
        faturamento_total += venda

    print(f"Faturamento total da semana: R$ {faturamento_total:.2f}")
faturamentoSemana()

#19 
def participantesFila():
    import math

    n = int(input("Digite o número de participantes (inteiro positivo): "))

    if n >= 0:
        fatorial = math.factorial(n)
        print(f"Existem {fatorial} formas diferentes de organizar a fila.")
    else:
        print("Por favor, digite um número inteiro positivo.")
participantesFila()

#20
def pesquisa():
    soma_notas = 0.0
    
    while True:
        nota = float(input("Digite uma nota (ou 0 para encerrar): "))
        if nota == 0:
            break
        soma_notas += nota

    print(f"Soma total das notas: {soma_notas}")
pesquisa()

#21
def estoque():

 produtos = ["Leite", "Leite", "Queijo", "requeijão", "Ovos"]
 print(produtos)

estoque()

#22
def maiorNota():

    notas = [10, 9.8, 2.3, 8.9, 3.3]
    maior = max(notas)

    print(maior)

#23
def categoriaGasto():
    gastos = [1200.50, 450.00, 320.80, 150.00, 89.90]

    totalGastos = sum(gastos)
    print(f"Soma total dos gastos mensais: R$ {totalGastos:.2f}")

categoriaGasto()

#24
def ordemChegada():
    ordem = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]
    inverso = list(reversed(ordem))
    print(inverso)
ordemChegada()

#25
def qntProdutos():
    produtos = ["Camiseta", "Calça Jeans", "Tênis", "Jaqueta", "Boné"]

    quantidade = len(produtos)
    print(f"Total de produtos cadastrados: {quantidade}")
qntProdutos()

#26
def codigoLista():
    codigos = [101, 102, 103, 104, 105]

codigobusca = int(input("Digite o código do produto a ser pesquisado: "))

if codigobusca in codigos:
    print(f"O código {codigobusca} está presente no sistema.")
else:
    print(f"O código {codigobusca} NÃO foi encontrado.")
codigoLista()

#27 
def meses():
    meses = (
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro",
)

print("Meses do ano:")
for mes in meses:
    print(mes)
meses()

#28
def temperaturas():
    temperaturas = (18.5, 25.0, 28.3, 21.2)

somatemperaturas = sum(temperaturas)
print(f"Soma das temperaturas do dia: {somatemperaturas:.1f}°C")
temperaturas()

#29
def resultadoVendas():
    vendas = (1500.0, 3200.50, 2700.0, 4100.20, 1900.0)

maiorVenda = max(vendas)
print(f"A maior venda registrada foi: R$ {maiorVenda:.2f}")
resultadoVendas()

#30 
def diasLetivos():
    dias_letivos = (
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
)

ultimoDia = dias_letivos[-1]
print(f"O último dia letivo da semana é: {ultimoDia}")
diasLetivos()
