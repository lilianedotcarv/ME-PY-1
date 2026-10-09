def contarCaractere(texto="programacao em python", caractere="a"):
    qtd = texto.count(caractere)
    print(f"O caractere '{caractere}' aparece {qtd} vez(es) na string '{texto}'.")
    return qtd
