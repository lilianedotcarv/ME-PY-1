class SaldoInsuficienteError(Exception):
    pass

def realizarSaqueBancario(saldoAtual, valorSaque):
    if valorSaque > saldoAtual:
        raise SaldoInsuficienteError(
            f"Operação negada! Saque de R$ {valorSaque:.2f} excede o saldo de R$ {saldoAtual:.2f}."
        )
    saldoAtual -= valorSaque
    return saldoAtual
