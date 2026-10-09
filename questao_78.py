def calcularMedia(n1, n2, n3):
    notas = [n1, n2, n3]
    for n in notas:
        if not isinstance(n, (int, float)):
            raise TypeError("Todas as notas informadas devem ser numéricas.")
        if not (0 <= n <= 10):
            raise ValueError(f"Nota inválida ({n}). As notas devem estar entre 0 e 10.")
    return sum(notas) / 3.0

def avaliarBoletim():
    try:
        n1 = float(input("Digite a 1ª nota: "))
        n2 = float(input("Digite a 2ª nota: "))
        n3 = float(input("Digite a 3ª nota: "))
        media = calcularMedia(n1, n2, n3)
        situacao = "Aprovado" if media >= 7.0 else "Reprovado"
        print(f"Média calculada: {media:.2f} | Situação: {situacao}")
    except ValueError as ve:
        print(f"Erro nas Notas: {ve}")
    except TypeError as te:
        print(f"Erro de Tipo: {te}")
