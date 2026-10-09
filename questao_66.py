def resolverSeuChico(cabecas=35, pernas=94):
    for coelhos in range(cabecas + 1):
        galinhas = cabecas - coelhos
        if (coelhos * 4 + galinhas * 2) == pernas:
            print(f"Seu Chico tem {galinhas} galinhas e {coelhos} coelhos em sua fazenda.")
            return galinhas, coelhos
