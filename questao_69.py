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
