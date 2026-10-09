import random

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
