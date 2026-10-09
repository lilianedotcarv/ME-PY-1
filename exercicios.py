import ast
import math
import random
import re
import traceback

#01
def livros():
    quantidade_livros = int(input("Digite a quantidade de livros lidos pela turma vencedora: "))
    print(f"A turma vencedora leu {quantidade_livros} livros!")

#02
def estudante():
    nome = input("Digite o nome completo do estudante: ")
    print(f"Seja bem-vindo(a) à instituição de ensino, {nome}!")

#03
def producao():
    setor_1 = float(input("Digite a quantidade produzida no Setor 1 (em kg): "))
    setor_2 = float(input("Digite a quantidade produzida no Setor 2 (em kg): "))
    producao_total = setor_1 + setor_2
    print(f"A produção total da cooperativa hoje foi de {producao_total:.2f} kg.")

#04
def medialuno():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2
    print(f"A média do estudante é: {media:.2f}")

#05
def compra():
    valor_compra = float(input("Digite o valor da compra (R$): "))
    if valor_compra >= 500.0:
        print("O cliente tem direito ao desconto promocional!")
    else:
        print("O cliente não atingiu o valor mínimo para o desconto.")

#06
def equipamento():
    codigo = int(input("Digite o código do equipamento: "))
    if codigo % 2 == 0:
        print(f"O equipamento {codigo} é PAR (Setor Administrativo).")
    else:
        print(f"O equipamento {codigo} é ÍMPAR (Setor Operacional).")

#07
def onibus():
    print("Lista de Assentos do Ônibus")
    for assento in range(1, 21):
        print(f"Assento número: {assento}")

#08
def alimentos():
    total_alimentos = 0.0
    for i in range(1, 6):
        quantidade = float(input(f"Digite a quantidade de alimentos arrecadada pelo voluntário {i} (em kg): "))
        total_alimentos += quantidade
    print(f"\nO total de alimentos arrecadados na campanha foi: {total_alimentos:.2f} kg")

#09
def livroslista():
    livros = []
    for i in range(1, 4):
        titulo = input(f"Digite o título do {i}º livro mais emprestado: ")
        livros.append(titulo)
    print("\nRelatório: Livros Mais Emprestados ")
    for i, livro in enumerate(livros, 1):
        print(f"{i}. {livro}")

#10
def semana():
    dias_da_semana = ("Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo")
    print(f"O primeiro dia da semana na escala é: {dias_da_semana[0]}")

#11
def bolsa_estudo():
    media = float(input("Digite a média final do estudante: "))
    if media >= 8.0:
        print("O estudante está APTO a participar da seleção para bolsas.")
    else:
        print("O estudante NÃO está apto a participar da seleção para bolsas.")

#12
def limite():
    limite = 80.0
    velocidade = float(input("Digite a velocidade registrada do veículo (km/h): "))
    if velocidade > limite:
        print(f"ALERTA: Velocidade de {velocidade:.1f} km/h ultrapassou o limite permitido de 80 km/h!")
    else:
        print(f"Velocidade de {velocidade:.1f} km/h dentro do limite permitido.")

#13
def setor_consumo():
    consumo_setor1 = float(input("Digite o consumo de energia do Setor 1 (kWh): "))
    consumo_setor2 = float(input("Digite o consumo de energia do Setor 2 (kWh): "))
    if consumo_setor1 > consumo_setor2:
        print(f"O Setor 1 apresentou o MAIOR consumo: {consumo_setor1:.2f} kWh.")
    elif consumo_setor2 > consumo_setor1:
        print(f"O Setor 2 apresentou o MAIOR consumo: {consumo_setor2:.2f} kWh.")
    else:
        print("Ambos os setores apresentaram consumo igual!")

#14
def visitantes():
    print("Controle de Visitantes da Feira de Ciências")
    for visitante in range(1, 51):
        print(f"Visitante nº {visitante}")

#15
def ex():
    print("sequencia de exercicios")
    for exercicio in range(1, 16):
        print(f"Exercicio: {exercicio}")

#16
def contagem():
    print("Iniciando Contagem")
    for segundo in range(10, 0, -1):
        print(segundo)
    print("Lançamento!")

#17
def cestasArrecadadas():
    total_cestas = 0
    for i in range(1, 11):
        qnt = int(input(f"Digite quantas cestas foram arrecadadas pelo voluntário {i}: "))
        total_cestas += qnt
    print(f"Total de cestas arrecadadas: {total_cestas}")

#18
def faturamentoSemana():
    faturamento_total = 0.0
    for dia in range(1, 8):
        venda = float(input(f"Digite o valor das vendas do dia {dia}: R$ "))
        faturamento_total += venda
    print(f"Faturamento total da semana: R$ {faturamento_total:.2f}")

#19
def participantesFila():
    n = int(input("Digite o número de participantes (inteiro positivo): "))
    if n >= 0:
        fatorial = math.factorial(n)
        print(f"Existem {fatorial} formas diferentes de organizar a fila.")
    else:
        print("Por favor, digite um número inteiro positivo.")

#20
def pesquisa():
    soma_notas = 0.0
    while True:
        nota = float(input("Digite uma nota (ou 0 para encerrar): "))
        if nota == 0:
            break
        soma_notas += nota
    print(f"Soma total das notas: {soma_notas}")

#21
def estoque():
    produtos = ["Leite", "Café", "Queijo", "Requeijão", "Ovos"]
    print("Produtos no estoque:", produtos)

#22
def maiorNota():
    notas = [10, 9.8, 2.3, 8.9, 3.3]
    maior = max(notas)
    print(f"A maior nota registrada é: {maior}")

#23
def categoriaGasto():
    gastos = [1200.50, 450.00, 320.80, 150.00, 89.90]
    totalGastos = sum(gastos)
    print(f"Soma total dos gastos mensais: R$ {totalGastos:.2f}")

#24
def ordemChegada():
    ordem = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]
    inverso = list(reversed(ordem))
    print("Ordem inversa de chegada:", inverso)

#25
def qntProdutos():
    produtos = ["Camiseta", "Calça Jeans", "Tênis", "Jaqueta", "Boné"]
    quantidade = len(produtos)
    print(f"Total de produtos cadastrados: {quantidade}")

#26
def codigoLista():
    codigos = [101, 102, 103, 104, 105]
    codigobusca = int(input("Digite o código do produto a ser pesquisado: "))
    if codigobusca in codigos:
        print(f"O código {codigobusca} está presente no sistema.")
    else:
        print(f"O código {codigobusca} NÃO foi encontrado.")

#27
def meses():
    meses_tupla = (
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    )
    print("Meses do ano:")
    for mes in meses_tupla:
        print(mes)

#28
def temperaturas():
    temp_tupla = (18.5, 25.0, 28.3, 21.2)
    somatemperaturas = sum(temp_tupla)
    print(f"Soma das temperaturas do dia: {somatemperaturas:.1f}°C")

#29
def resultadoVendas():
    vendas = (1500.0, 3200.50, 2700.0, 4100.20, 1900.0)
    maiorVenda = max(vendas)
    print(f"A maior venda registrada foi: R$ {maiorVenda:.2f}")

#30
def diasLetivos():
    dias_letivos = (
        "Segunda-feira", "Terça-feira", "Quarta-feira",
        "Quinta-feira", "Sexta-feira"
    )
    ultimoDia = dias_letivos[-1]
    print(f"O último dia letivo da semana é: {ultimoDia}")

#31
def cadastroFuncionario():
    funcionario = {
        "nome": "João Santos",
        "idade": 30,
        "setor": "Logística"
    }
    print("Dados do funcionário:")
    for chave, valor in funcionario.items():
        print(f"{chave.capitalize()}: {valor}")

#32
def cadastroPaciente():
    paciente = {"nome": "Maria Oliveira"}
    paciente["idade"] = 42
    print("Cadastro do paciente:", paciente)

#33
def chavesLivro():
    livro = {
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
        "ano": 1899,
        "editora": "Livraria Garnett"
    }
    print("Informações disponíveis no cadastro do livro:")
    for chave in livro.keys():
        print(f"- {chave}")

#34
def consultarNota():
    notas = {
        "Ana": 8.5,
        "Bruno": 7.0,
        "Carla": 9.2,
        "Daniel": 6.5
    }
    nome = input("Digite o nome do estudante para consultar a nota: ")
    if nome in notas:
        print(f"A nota de {nome} é: {notas[nome]}")
    else:
        print("Estudante não encontrado no sistema.")

#35
def cadastrarProdutos():
    estoque = {}
    for i in range(1, 4):
        produto = input(f"Digite o nome do {i}º produto: ")
        quantidade = int(input(f"Digite a quantidade de {produto}: "))
        estoque[produto] = quantidade
    print("\nProdutos e quantidades cadastradas:")
    for prod, qtd in estoque.items():
        print(f"{prod}: {qtd} unidades")

#36
def sorteioPremio():
    vencedor = random.randint(1, 50)
    print(f"O número sorteado para o prêmio foi: {vencedor}")

#37
def rolarDado():
    resultado = random.randint(1, 6)
    print(f"O dado rolou e caiu no número: {resultado}")

#38
def indicarLivro():
    livros = ["1984", "O Hobbit", "O Pequeno Príncipe", "Capitães da Areia", "A Hora da Estrela"]
    livroSorteado = random.choice(livros)
    print(f"Sugestão de leitura de hoje: '{livroSorteado}'")

#39
def adivinhaRapida():
    numero_secreto = random.randint(1, 10)
    palpite = int(input("Adivinhe o número sorteado (entre 1 e 10): "))
    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
    else:
        print(f"Que pena! O número correto era {numero_secreto}.")

#40
def adivinhaDicas():
    numeroSecreto = random.randint(1, 100)
    tentativas = 0
    print("Tente adivinhar o número entre 1 e 100!")
    while True:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1
        if palpite == numeroSecreto:
            print(f"Parabéns! Você acertou em {tentativas} tentativa(s)!")
            break
        elif palpite < numeroSecreto:
            print("O número procurado é MAIOR.")
        else:
            print("O número procurado é MENOR.")

#41
def matrizSala():
    sala = [
        ["Ana", "Bruno"],
        ["Carla", "Daniel"]
    ]
    print("Disposição dos alunos na sala (2x2):")
    for fileira in sala:
        print(" | ".join(fileira))

#42
def somaMatriz():
    producao = [
        [10, 20, 30],
        [15, 25, 35],
        [40, 50, 60]
    ]
    soma_total = sum(sum(linha) for linha in producao)
    print(f"Soma de todos os valores da matriz: {soma_total}")

#43
def maiorValorMatriz():
    dados = [
        [12, 45, 23],
        [67, 89, 34],
        [54, 11, 78]
    ]
    maior = max(max(linha) for linha in dados)
    print(f"O maior valor na matriz é: {maior}")

#44
def menorCustoMatriz():
    custos = [
        [150.0, 230.5, 99.0],
        [450.0, 88.5, 120.0],
        [310.0, 75.0, 200.0]
    ]
    menor = min(min(linha) for linha in custos)
    print(f"O menor custo registrado é: R$ {menor:.2f}")

#45
def diagonalPrincipal():
    matriz = [
        [5, 2, 9],
        [1, 7, 3],
        [8, 4, 6]
    ]
    elementos_diagonal = [matriz[i][i] for i in range(len(matriz))]
    print("Elementos da diagonal principal:", elementos_diagonal)

#46
def somaDiagonal():
    matriz = [
        [10, 2, 3],
        [4, 20, 6],
        [7, 8, 30]
    ]
    soma = sum(matriz[i][i] for i in range(len(matriz)))
    print(f"Soma dos elementos da diagonal principal: {soma}")

#47
def contarPositivos():
    matriz = [
        [-5, 10, -3],
        [8, -2, 15],
        [0, 7, -1]
    ]
    positivos = sum(1 for linha in matriz for val in linha if val > 0)
    print(f"Quantidade de valores positivos: {positivos}")

#48
def matrizIdentidade():
    ordem = 3
    matriz = [[1 if i == j else 0 for j in range(ordem)] for i in range(ordem)]
    print("Matriz Identidade 3x3:")
    for linha in matriz:
        print(linha)

#49
def cadastrarAlunos():
    alunos = {}
    for i in range(1, 6):
        nome = input(f"Digite o nome do {i}º aluno: ")
        nota = float(input(f"Digite a nota de {nome}: "))
        alunos[nome] = nota
    print("\nRegistros de Alunos:")
    for nome, nota in alunos.items():
        print(f"Aluno: {nome} | Nota: {nota:.1f}")

#50
def desempenhoTurma():
    alunos = {}
    for i in range(1, 6):
        nome = input(f"Digite o nome do {i}º aluno: ")
        nota = float(input(f"Digite a nota de {nome}: "))
        alunos[nome] = nota
    media_turma = sum(alunos.values()) / len(alunos)
    aprovados = [nome for nome, nota in alunos.items() if nota >= 7.0]
    print(f"\nMédia Geral da Turma: {media_turma:.2f}")
    print("Alunos Aprovados (Nota >= 7.0):", ", ".join(aprovados) if aprovados else "Nenhum")

#51
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

#52
def controleFarmacia():
    estoque = {}
    print("--- Cadastro de Medicamentos ---")
    for i in range(1, 6):
        med = input(f"Digite o nome do {i}º medicamento: ").strip().capitalize()
        qtd = int(input(f"Digite a quantidade de {med} em estoque: "))
        estoque[med] = qtd
    print("\n--- Consulta de Estoque ---")
    busca = input("Digite o nome do medicamento para consultar: ").strip().capitalize()
    if busca in estoque:
        print(f"Estoque de {busca}: {estoque[busca]} unidade(s).")
    else:
        print("Medicamento não cadastrado no sistema.")

#53
def sortearLider():
    participantes = ["Ana", "Carlos", "Pedro", "Beatriz", "Maria"]
    lider = random.choice(participantes)
    print(f"O estudante sorteado para ser o líder da equipe é: {lider}")

#54
def ocupacaoEstacionamento():
    estacionamento = [
        [1, 0, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]
    ocupadas = sum(linha.count(1) for linha in estacionamento)
    livres = sum(linha.count(0) for linha in estacionamento)
    print(f"Vagas Ocupadas: {ocupadas}")
    print(f"Vagas Livres: {livres}")

#55
def desempenhoEscolar():
    disciplinas = ("Matemática", "Português")
    turma = {}
    qtd_alunos = int(input("Digite a quantidade de alunos a cadastrar: "))
    for i in range(qtd_alunos):
        nome = input(f"\nDigite o nome do {i+1}º aluno: ")
        nota_mat = float(input(f"Nota em {disciplinas[0]}: "))
        nota_port = float(input(f"Nota em {disciplinas[1]}: "))
        turma[nome] = {
            disciplinas[0]: nota_mat,
            disciplinas[1]: nota_port
        }
    print("\n--- RESULTADOS FINAIS ---")
    print(f"Disciplinas avaliadas: {disciplinas[0]} e {disciplinas[1]}\n")
    for aluno, notas in turma.items():
        media = (notas[disciplinas[0]] + notas[disciplinas[1]]) / 2
        situacao = "Aprovado" if media >= 7.0 else "Reprovado"
        print(f"Aluno: {aluno} | Média: {media:.2f} | Situação: {situacao}")

#56
def graosXadrez():
    total_graos = (2 ** 64) - 1
    print(f"O número total de grãos de trigo esperados é: {total_graos:,}")

#57
def contarCaractere(texto="programacao em python", caractere="a"):
    qtd = texto.count(caractere)
    print(f"O caractere '{caractere}' aparece {qtd} vez(es) na string '{texto}'.")
    return qtd

#58
def calcularGorjeta(valor_conta=150.0):
    gorjeta = valor_conta * 0.10
    print(f"Valor da conta: R$ {valor_conta:.2f} | Gorjeta (10%): R$ {gorjeta:.2f}")
    return gorjeta

#59
def compararNumeros(num1=4, num2=8):
    if num1 % 2 == 0 and num2 % 2 == 0:
        resultado = min(num1, num2)
    else:
        resultado = max(num1, num2)
    print(f"Resultado da comparação entre {num1} e {num2}: {resultado}")
    return resultado

#60
def fahrenheitParaCelsius(f=100.0):
    celsius = (5 / 9) * (f - 32)
    print(f"{f:.1f}°F equivale a {celsius:.2f}°C")
    return celsius

#61
def inverterString(texto):
    return texto[::-1]

#62
def eNumeroPerfeito(numero):
    if numero <= 0:
        return False
    divisores = [i for i in range(1, numero) if numero % i == 0]
    ePerfeito = sum(divisores) == numero
    print(f"O número {numero} é perfeito? {ePerfeito}")
    return ePerfeito

#63
def receberNumeros():
    numeros = []
    print("Digite 5 números reais:")
    for i in range(1, 6):
        num = float(input(f"Digite o {i}º número: "))
        numeros.append(num)
    return numeros

def encontrarMaior(numeros):
    return max(numeros)

def encontrarMenor(numeros):
    return min(numeros)

#64
def somaAjustada(a, b, c):
    soma = a + b + c
    if soma <= 21:
        return soma
    if soma > 21 and (a == 11 or b == 11 or c == 11):
        soma -= 10
    if soma > 21:
        return -1
    return soma

#65
def calcularCubo(numero):
    return numero ** 3

def calcularDivisaoCubo(numero):
    if numero % 3 == 0:
        return calcularCubo(numero)
    return False

#66
def resolverSeuChico(cabecas=35, pernas=94):
    for coelhos in range(cabecas + 1):
        galinhas = cabecas - coelhos
        if (coelhos * 4 + galinhas * 2) == pernas:
            print(f"Seu Chico tem {galinhas} galinhas e {coelhos} coelhos em sua fazenda.")
            return galinhas, coelhos

#67
def cadastrarIdadeUsuario():
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if idade < 0:
                raise ValueError("A idade não pode ser um número negativo.")
            print(f"Idade {idade} cadastrada com sucesso!")
            return idade
        except ValueError as e:
            print(f"Entrada inválida ({e}). Por favor, tente novamente.\n")

#68
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

#69
def lerRelatorioVendas():
    arquivo = None
    try:
        arquivo = open("relatorio_vendas.txt", "r", encoding="utf-8")
        conteudo = arquivo.read()
        print("Conteúdo do Relatório:")
        print(conteudo)
    except FileNotFoundError:
        print("Erro: O arquivo 'relatorio_vendas.txt' não foi encontrado.")
    finally:
        if arquivo and not arquivo.closed:
            arquivo.close()
        print("Encerramento do recurso do relatório concluído.")

#70
def buscarPermissao(perfis, perfil, indice):
    try:
        return perfis[perfil][indice]
    except (KeyError, IndexError):
        return "acesso_restrito"

#71
class SaldoInsuficienteError(Exception):
    pass

def realizarSaqueBancario(saldoAtual, valorSaque):
    if valorSaque > saldoAtual:
        raise SaldoInsuficienteError(
            f"Operação negada! Saque de R$ {valorSaque:.2f} excede o saldo de R$ {saldoAtual:.2f}."
        )
    saldoAtual -= valorSaque
    return saldoAtual

#72
def parseCpf(cpf):
    cpfLimpo = cpf.replace(".", "").replace("-", "").strip()
    if not cpfLimpo.isdigit() or len(cpfLimpo) != 11:
        raise ValueError("CPF inválido! Deve conter exatamente 11 dígitos numéricos.")
    return cpfLimpo

def mainCpf():
    try:
        cpfUsuario = "123.456.789-00"
        cpfValido = parseCpf(cpfUsuario)
        print(f"CPF formatado com sucesso no main: {cpfValido}")
    except ValueError as e:
        print(f"Erro processado na interface principal: {e}")

#73
def aplicarDescontoPrecos(listaPrecosStr):
    precosComDesconto = []
    for item in listaPrecosStr:
        try:
            preco = float(item)
        except ValueError:
            print(f"Falha ao converter '{item}' para número.")
        else:
            precoDesconto = preco * 0.90
            precosComDesconto.append(precoDesconto)
            print(f"Preço R$ {preco:.2f} com 10% de desconto -> R$ {precoDesconto:.2f}")
    return precosComDesconto

#74
def RotaObterProduto(produtoId):
    bancoProdutos = {1: "Notebook", 2: "Mouse", 3: "Teclado"}
    try:
        if produtoId == "erroSimulado":
            raise RuntimeError("Falha grave interna")
        produto = bancoProdutos[produtoId]
        return {"status": 200, "body": {"id": produtoId, "nome": produto}}
    except KeyError:
        return {"status": 404, "body": "HTTP Status 404: Produto não encontrado"}
    except Exception:
        return {"status": 500, "body": "HTTP Status 500: Erro interno do servidor"}

#75
def mockConexaoAPI():
    if random.choice([True, False]):
        raise ConnectionError("Falha de comunicação com o servidor da API.")
    return "Sucesso: Conectado à API!"

def conectarComResiliencia():
    maxTentativas = 3
    for tentativa in range(1, maxTentativas + 1):
        try:
            print(f"Tentativa {tentativa} de conexão...")
            resposta = mockConexaoAPI()
            print(resposta)
            return True
        except ConnectionError as e:
            print(f"Aviso de erro na tentativa {tentativa}: {e}")
    print("Erro: Limite de 3 tentativas atingido. Encerrando execução com segurança.")
    return False

#76
def processarEstatistica(elementos):
    processados = []
    for i, elemento in enumerate(elementos):
        try:
            valor = float(elemento)
            if valor < 0:
                raise ValueError("Valores negativos não são permitidos no cálculo.")
            processados.append(valor ** 2)
        except (TypeError, ValueError):
            print(f"\n[AUDITORIA] Erro registrado no índice {i} para o elemento: '{elemento}'")
            traceback.print_exc(limit=1)
            print("--------------------------------------------------\n")
    return processados

#77
def realizarSaque(saldo, valorSaque):
    if valorSaque <= 0:
        raise ValueError("O valor do saque deve ser estritamente positivo.")
    if valorSaque > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente para realizar o saque.")
    return saldo - valorSaque

def programaCaixaEletronico():
    saldoAtual = 500.0
    try:
        valor = float(input("Digite o valor que deseja sacar: R$ "))
        novoSaldo = realizarSaque(saldoAtual, valor)
        print(f"Saque efetuado com sucesso! Novo saldo: R$ {novoSaldo:.2f}")
    except ValueError as ve:
        print(f"Erro de Validação: {ve}")
    except SaldoInsuficienteError as se:
        print(f"Erro de Saldo: {se}")

#78
def calcularMedia(n1, n2, n3):
    notas = [n1, n2, n3]
    for n in notas:
        if not isinstance(n, (int, float)):
            raise TypeError("Todas as notas informadas devem ser numéricas.")
        if not (0 <= n <= 10):
            raise ValueError(f"Nota inválida ({n}). As notas devem estar entre 0 e 10.")
    return sum(notas) / 3.0

def avaliarBoletim():
    try:
        n1 = float(input("Digite a 1ª nota: "))
        n2 = float(input("Digite a 2ª nota: "))
        n3 = float(input("Digite a 3ª nota: "))
        media = calcularMedia(n1, n2, n3)
        situacao = "Aprovado" if media >= 7.0 else "Reprovado"
        print(f"Média calculada: {media:.2f} | Situação: {situacao}")
    except ValueError as ve:
        print(f"Erro nas Notas: {ve}")
    except TypeError as te:
        print(f"Erro de Tipo: {te}")

#79
def cadastrarProduto(nome, preco, quantidade):
    if not isinstance(nome, str) or not nome.strip():
        raise ValueError("O nome do produto não pode ser vazio.")
    if preco <= 0:
        raise ValueError("O preço do produto deve ser maior que zero.")
    if quantidade < 0:
        raise ValueError("A quantidade do produto não pode ser negativa.")
    return f"Sucesso: Produto '{nome.strip()}' cadastrado com sucesso!"

#80
class ProdutoInvalidoError(Exception):
    pass

class ValorInvalidoError(Exception):
    pass

class QuantidadeInvalidaError(Exception):
    pass

def registrarVenda(produto, preco, quantidade):
    if not produto or not produto.strip():
        raise ProdutoInvalidoError("O nome do produto não pode estar vazio.")
    if preco <= 0:
        raise ValorInvalidoError("O preço unitário deve ser maior que zero.")
    if not isinstance(quantidade, int) or quantidade <= 0:
        raise QuantidadeInvalidaError("A quantidade vendida deve ser um número inteiro positivo.")

    total = preco * quantidade
    return {
        "produto": produto.strip().capitalize(),
        "preco": preco,
        "quantidade": quantidade,
        "total": total
    }

def gerarRelatorio(vendas):
    if not vendas:
        print("\nNenhuma venda válida foi registrada no período.")
        return

    qtdTotalVendas = len(vendas)
    faturamentoTotal = sum(v["total"] for v in vendas)
    ticketMedio = faturamentoTotal / qtdTotalVendas

    contagemProdutos = {}
    for v in vendas:
        p = v["produto"]
        contagemProdutos[p] = contagemProdutos.get(p, 0) + v["quantidade"]

    produtoMaisVendido = max(contagemProdutos, key=contagemProdutos.get)

    print("\n================ RELATÓRIO DE VENDAS ================")
    print(f"Quantidade total de vendas realizadas: {qtdTotalVendas}")
    print(f"Produto mais vendido: {produtoMaisVendido} ({contagemProdutos[produtoMaisVendido]} unidades)")
    print(f"Faturamento total da loja: R$ {faturamentoTotal:.2f}")
    print(f"Ticket médio por venda: R$ {ticketMedio:.2f}")
    print("=====================================================")

def sistemaLojaVirtual():
    vendasRegistradas = []
    print("--- Registro de Vendas - Loja Virtual ---")

    while True:
        try:
            produto = input("\nDigite o nome do produto (ou 'fim' para encerrar): ").strip()
            if produto.lower() == "fim":
                break

            preco = float(input(f"Digite o preço unitário de '{produto}': R$ "))
            quantidade = int(input(f"Digite a quantidade vendida de '{produto}': "))

            venda = registrarVenda(produto, preco, quantidade)
        except ProdutoInvalidoError as pie:
            print(f"Erro no Produto: {pie}")
            with open("log_erros.txt", "a", encoding="utf-8") as f_err:
                f_err.write(f"ProdutoInvalidoError: {pie}\n")
        except ValorInvalidoError as vie:
            print(f"Erro no Preço: {vie}")
            with open("log_erros.txt", "a", encoding="utf-8") as f_err:
                f_err.write(f"ValorInvalidoError: {vie}\n")
        except QuantidadeInvalidaError as qie:
            print(f"Erro na Quantidade: {qie}")
            with open("log_erros.txt", "a", encoding="utf-8") as f_err:
                f_err.write(f"QuantidadeInvalidaError: {qie}\n")
        except ValueError:
            print("Erro de Digitação: Certifique-se de digitar números válidos para preço e quantidade.")
            with open("log_erros.txt", "a", encoding="utf-8") as f_err:
                f_err.write("ValueError: Entrada não numérica\n")
        else:
            vendasRegistradas.append(venda)
            print(f"Venda de '{venda['produto']}' inserida com sucesso!")
            with open("vendas.txt", "a", encoding="utf-8") as f_vendas:
                f_vendas.write(f"{venda['produto']},{venda['preco']},{venda['quantidade']},{venda['total']}\n")
        finally:
            print("Processamento do registro finalizado.")

    gerarRelatorio(vendasRegistradas)