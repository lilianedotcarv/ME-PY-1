import random

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

cadastroFuncionario()


#32
def cadastroPaciente():
    paciente = {"nome": "Maria Oliveira"}
    
    paciente["idade"] = 42
    
    print("Cadastro do paciente:", paciente)

cadastroPaciente()


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

chavesLivro()


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

consultarNota()


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

cadastrarProdutos()


#36
def sorteioPremio():
    vencedor = random.randint(1, 50)
    print(f"O número sorteado para o prêmio foi: {vencedor}")

sorteioPremio()


#37
def rolarDado():
    resultado = random.randint(1, 6)
    print(f"O dado rolou e caiu no número: {resultado}")

rolarDado()


#38
def indicarLivro():
    livros = ["1984", "O Hobbit", "O Pequeno Príncipe", "Capitães da Areia", "A Hora da Estrela"]
    livroSorteado = random.choice(livros)
    print(f"Sugestão de leitura de hoje: '{livroSorteado}'")

indicarLivro()


#39
def adivinhaRapida():
    numero_secreto = random.randint(1, 10)
    palpite = int(input("Adivinhe o número sorteado (entre 1 e 10): "))
    
    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
    else:
        print(f"Que pena! O número correto era {numero_secreto}.")

adivinhaRapida()


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

adivinhaDicas()


#41
def matrizSala():
    sala = [
        ["Ana", "Bruno"],
        ["Carla", "Daniel"]
    ]
    
    print("Disposição dos alunos na sala (2x2):")
    for fileira in sala:
        print(" | ".join(fileira))

matrizSala()


#42
def somaMatriz():
    producao = [
        [10, 20, 30],
        [15, 25, 35],
        [40, 50, 60]
    ]
    
    soma_total = sum(sum(linha) for linha in producao)
    print(f"Soma de todos os valores da matriz: {soma_total}")

somaMatriz()


#43
def maiorValorMatriz():
    dados = [
        [12, 45, 23],
        [67, 89, 34],
        [54, 11, 78]
    ]
    
    maior = max(max(linha) for linha in dados)
    print(f"O maior valor na matriz é: {maior}")

maiorValorMatriz()


#44
def menorCustoMatriz():
    custos = [
        [150.0, 230.5, 99.0],
        [450.0, 88.5, 120.0],
        [310.0, 75.0, 200.0]
    ]
    
    menor = min(min(linha) for linha in custos)
    print(f"O menor custo registrado é: R$ {menor:.2f}")

menorCustoMatriz()


#45
def diagonalPrincipal():
    matriz = [
        [5, 2, 9],
        [1, 7, 3],
        [8, 4, 6]
    ]
    
    elementos_diagonal = [matriz[i][i] for i in range(len(matriz))]
    print("Elementos da diagonal principal:", elementos_diagonal)

diagonalPrincipal()


#46
def somaDiagonal():
    matriz = [
        [10, 2, 3],
        [4, 20, 6],
        [7, 8, 30]
    ]
    
    soma = sum(matriz[i][i] for i in range(len(matriz)))
    print(f"Soma dos elementos da diagonal principal: {soma}")

somaDiagonal()


#47
def contarPositivos():
    matriz = [
        [-5, 10, -3],
        [8, -2, 15],
        [0, 7, -1]
    ]
    
    positivos = sum(1 for linha in matriz for val in linha if val > 0)
    print(f"Quantidade de valores positivos: {positivos}")

contarPositivos()


#48
def matrizIdentidade():
    ordem = 3
    matriz = [[1 if i == j else 0 for j in range(ordem)] for i in range(ordem)]
    
    print("Matriz Identidade 3x3:")
    for linha in matriz:
        print(linha)

matrizIdentidade()


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

cadastrarAlunos()


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

desempenhoTurma()


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

monitorEstufa()


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

controleFarmacia()


#53
def sortearLider():
    participantes = ["Ana", "Carlos", "Pedro", "Beatriz", "Maria"]
    lider = random.choice(participantes)
    print(f"O estudante sorteado para ser o líder da equipe é: {lider}")

sortearLider()


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

ocupacaoEstacionamento()


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

desempenhoEscolar()


#56
def graosXadrez():
    total_graos = (2 ** 64) - 1
    print(f"O número total de grãos de trigo esperados é: {total_graos:,}")

graosXadrez()


#57
def contarCaractere(texto="programacao em python", caractere="a"):
    qtd = texto.count(caractere)
    print(f"O caractere '{caractere}' aparece {qtd} vez(es) na string '{texto}'.")
    return qtd

contarCaractere()


#58
def calcularGorjeta(valor_conta=150.0):
    gorjeta = valor_conta * 0.10
    print(f"Valor da conta: R$ {valor_conta:.2f} | Gorjeta (10%): R$ {gorjeta:.2f}")
    return gorjeta

calcularGorjeta()


#59
def compararNumeros(num1=4, num2=8):
    if num1 % 2 == 0 and num2 % 2 == 0:
        resultado = min(num1, num2)
    else:
        resultado = max(num1, num2)
    print(f"Resultado da comparação entre {num1} e {num2}: {resultado}")
    return resultado

compararNumeros()


#60
def fahrenheitParaCelsius(f=100.0):
    celsius = (5 / 9) * (f - 32)
    print(f"{f:.1f}°F equivale a {celsius:.1f}°C")
    return celsius

fahrenheitParaCelsius()