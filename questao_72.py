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
