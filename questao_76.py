import traceback

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
