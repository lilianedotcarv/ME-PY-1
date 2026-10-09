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
