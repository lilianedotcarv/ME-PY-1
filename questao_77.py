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
