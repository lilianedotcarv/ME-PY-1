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
