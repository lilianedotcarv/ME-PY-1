import random
import traceback

# 61
def fahrenheitParaCelsius(f):
    celsius = (5 / 9) * (f - 32)
    print(f"{f:.1f}°F equivale a {celsius:.2f}°C")
    return celsius

fahrenheitParaCelsius(100.0)

# 62
def inverterString(texto):
    return texto[::-1]


stringsParaInverter = [
    "python2023",
    "0203programacao2023",
    "luz azul",
    "arara rara",
    "anotaram a data da maratona",
]

print("Strings invertidas:")
for s in stringsParaInverter:
    print(f"'{s}' -> '{inverterString(s)}'")


# 63
def eNumeroPerfeito(numero):
    if numero <= 0:
        return False
    divisores = [i for i in range(1, numero) if numero % i == 0]
    ePerfeito = sum(divisores) == numero
    print(f"O número {numero} é perfeito? {ePerfeito}")
    return ePerfeito


eNumeroPerfeito(6)
eNumeroPerfeito(28)
eNumeroPerfeito(12)


# 64
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

# 65
def somaAjustada(a, b, c):
    soma = a + b + c
    if soma <= 21:
        return soma
    if soma > 21 and (a == 11 or b == 11 or c == 11):
        soma -= 10
    if soma > 21:
        return -1
    return soma


print("Soma Ajustada (5, 6, 7):", somaAjustada(5, 6, 7))
print("Soma Ajustada (10, 11, 8):", somaAjustada(10, 11, 8))
print("Soma Ajustada (10, 10, 11):", somaAjustada(10, 10, 11))
print("Soma Ajustada (10, 10, 10):", somaAjustada(10, 10, 10))


# 66
def calcularCubo(numero):
    return numero**3


def calcularDivisaoCubo(numero):
    if numero % 3 == 0:
        return calcularCubo(numero)
    return False


print("Cubo de 9 (divisível por 3):", calcularDivisaoCubo(9))
print("Cubo de 4 (não divisível por 3):", calcularDivisaoCubo(4))


# 67
def resolverSeuChico(cabecas=35, pernas=94):
    for coelhos in range(cabecas + 1):
        galinhas = cabecas - coelhos
        if (coelhos * 4 + galinhas * 2) == pernas:
            print(
                f"Seu Chico tem {galinhas} galinhas e {coelhos} coelhos em sua fazenda."
            )
            return galinhas, coelhos


resolverSeuChico()


# 68
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


cadastrarIdadeUsuario()


# 69
def dividirLucrosTrimestre():
    try:
        lucro = float(input("Digite o lucro total do trimestre: R$ "))
        acionistas = int(input("Digite a quantidade N de acionistas: "))

        divisao = lucro / acionistas
        print(f"Cada acionista receberá: R$ {divisao:.2f}")
    except ZeroDivisionError:
        print("Erro: A quantidade de acionistas não pode ser zero!")
    except ValueError:
        print(
            "Erro: Por favor, informe apenas números válidos para o cálculo."
        )

dividirLucrosTrimestre()


# 70
def lerRelatorioVendas():
    arquivo = None
    try:
        arquivo = open("relatorioVendas.txt", "r", encoding="utf-8")
        conteudo = arquivo.read()
        print("Conteúdo do Relatório:")
        print(conteudo)
    except FileNotFoundError:
        print("Erro: O arquivo 'relatorioVendas.txt' não foi encontrado.")
    finally:
        if arquivo and not arquivo.closed:
            arquivo.close()
        print("Encerramento do recurso do relatório concluído.")

lerRelatorioVendas()

# 71
def buscarPermissao(perfis, perfil, indice):
    try:
        return perfis[perfil][indice]
    except (KeyError, IndexError):
        return "acesso_restrito"

perfisDados = {
    "admin": ["ler", "escrever", "excluir"],
    "operador": ["ler", "escrever"],
}
print("Permissão admin[1]:", buscarPermissao(perfisDados, "admin", 1))
print("Permissão visitante[0]:", buscarPermissao(perfisDados, "visitante", 0))
print("Permissão operador[5]:", buscarPermissao(perfisDados, "operador", 5))

# 72
class SaldoInsuficienteError(Exception):
    pass

def realizarSaqueBancario(saldoAtual, valorSaque):
    if valorSaque > saldoAtual:
        raise SaldoInsuficienteError(
            f"Operação negada! Saque de R$ {valorSaque:.2f} excede o saldo de R$ {saldoAtual:.2f}."
        )
    saldoAtual -= valorSaque
    return saldoAtual

try:
    saldo = 100.00
    saldo = realizarSaqueBancario(saldo, 150.00)
except SaldoInsuficienteError as e:
    print(f"Exceção capturada: {e}")

# 73
def parseCpf(cpf):
    cpfLimpo = cpf.replace(".", "").replace("-", "").strip()
    if not cpfLimpo.isdigit() or len(cpfLimpo) != 11:
        raise ValueError(
            "CPF inválido! Deve conter exatamente 11 dígitos numéricos."
        )
    return cpfLimpo

def mainCpf():
    try:
        cpfUsuario = "123.456.789-00"
        cpfValido = parseCpf(cpfUsuario)
        print(f"CPF formatado com sucesso no main: {cpfValido}")
    except ValueError as e:
        print(f"Erro processado na interface principal: {e}")

mainCpf()

# 74
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
            print(
                f"Preço R$ {preco:.2f} com 10% de desconto -> R$ {precoDesconto:.2f}"
            )
    return precosComDesconto

aplicarDescontoPrecos(["100.0", "50.0", "inválido", "200.0"])

# 75
def RotaObterProduto(produtoId):
    bancoProdutos = {1: "Notebook", 2: "Mouse", 3: "Teclado"}
    try:
        if produtoId == "erroSimulado":
            raise RuntimeError("Falha grave interna")
        produto = bancoProdutos[produtoId]
        return {"status": 200, "body": {"id": produtoId, "nome": produto}}
    except KeyError:
        return {
            "status": 404,
            "body": "HTTP Status 404: Produto não encontrado",
        }
    except Exception:
        return {
            "status": 500,
            "body": "HTTP Status 500: Erro interno do servidor",
        }

print(RotaObterProduto(1))
print(RotaObterProduto(99))
print(RotaObterProduto("erroSimulado"))

# 76
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

    print(
        "Erro: Limite de 3 tentativas atingido. Encerrando execução com segurança."
    )
    return False

conectarComResiliencia()


# 77
def processarEstatistica(elementos):
    processados = []
    for i, elemento in enumerate(elementos):
        try:
            valor = float(elemento)
            if valor < 0:
                raise ValueError(
                    "Valores negativos não são permitidos no cálculo."
                )
            processados.append(valor**2)
        except (TypeError, ValueError):
            print(
                f"\n[AUDITORIA] Erro registrado no índice {i} para o elemento: '{elemento}'"
            )
            traceback.print_exc(limit=1)
            print("--------------------------------------------------\n")
    return processados

processarEstatistica([10, "20", -5, None, "dadosInvalidos", 4])

# 78
def realizarSaque(saldo, valorSaque):
    if valorSaque <= 0:
        raise ValueError("O valor do saque deve ser estritamente positivo.")
    if valorSaque > saldo:
        raise SaldoInsuficienteError(
            "Saldo insuficiente para realizar o saque."
        )
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

programaCaixaEletronico()


# 79
def calcularMedia(n1, n2, n3):
    notas = [n1, n2, n3]
    for n in notas:
        if not isinstance(n, (int, float)):
            raise TypeError("Todas as notas informadas devem ser numéricas.")
        if not (0 <= n <= 10):
            raise ValueError(
                f"Nota inválida ({n}). As notas devem estar entre 0 e 10."
            )
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

avaliarBoletim()

# 80
def cadastrarProduto(nome, preco, quantidade):
    if not isinstance(nome, str) or not nome.strip():
        raise ValueError("O nome do produto não pode ser vazio.")
    if preco <= 0:
        raise ValueError("O preço do produto deve ser maior que zero.")
    if quantidade < 0:
        raise ValueError("A quantidade do produto não pode ser negativa.")
    return f"Sucesso: Produto '{nome.strip()}' cadastrado com sucesso!"

try:
    msg = cadastrarProduto("Teclado Mecânico", 250.00, 15)
    print(msg)
except ValueError as e:
    print(f"Erro de Cadastro: {e}")


# 81
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
        raise QuantidadeInvalidaError(
            "A quantidade vendida deve ser um número inteiro positivo."
        )

    total = preco * quantidade
    return {
        "produto": produto.strip().capitalize(),
        "preco": preco,
        "quantidade": quantidade,
        "total": total,
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
    print(
        f"Produto mais vendido: {produtoMaisVendido} ({contagemProdutos[produtoMaisVendido]} unidades)"
    )
    print(f"Faturamento total da loja: R$ {faturamentoTotal:.2f}")
    print(f"Ticket médio por venda: R$ {ticketMedio:.2f}")
    print("=====================================================")

def sistemaLojaVirtual():
    vendasRegistradas = []
    print("--- Registro de Vendas - Loja Virtual ---")

    while True:
        try:
            produto = input(
                "\nDigite o nome do produto (ou 'fim' para encerrar): "
            ).strip()
            if produto.lower() == "fim":
                break

            preco = float(input(f"Digite o preço unitário de '{produto}': R$ "))
            quantidade = int(
                input(f"Digite a quantidade vendida de '{produto}': ")
            )

            venda = registrarVenda(produto, preco, quantidade)
        except ProdutoInvalidoError as pie:
            print(f"Erro no Produto: {pie}")
        except ValorInvalidoError as vie:
            print(f"Erro no Preço: {vie}")
        except QuantidadeInvalidaError as qie:
            print(f"Erro na Quantidade: {qie}")
        except ValueError:
            print(
                "Erro de Digitação: Certifique-se de digitar números válidos para preço e quantidade."
            )
        else:
            vendasRegistradas.append(venda)
            print(f"Venda de '{venda['produto']}' inserida com sucesso!")
        finally:
            print("Processamento do registro finalizado.")

    gerarRelatorio(vendasRegistradas)

sistemaLojaVirtual()