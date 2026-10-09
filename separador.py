import ast
import re
from pathlib import Path

arquivo_origem = Path("exercicios.py")
pasta_saida = Path("exercicios_separados")
pasta_saida.mkdir(exist_ok=True)

BIBLIOTECAS = {
    "math": "import math",
    "random": "import random",
    "traceback": "import traceback",
}

conteudo = arquivo_origem.read_text(encoding="utf-8")

# Regex flexível: aceita #01, # 01, #Questão 31, # Exercicio 31, #31 - Título, #31: etc.
padrao = re.compile(
    r"(?m)^[ \t]*\#[ \t]*(?:questã[o]|questao|exercí[c]io|exercicio|q|ex)?[ \t]*(\d+)\b",
    re.IGNORECASE
)

marcadores = list(padrao.finditer(conteudo))

if not marcadores:
    raise SystemExit(
        "Nenhum marcador encontrado. Verifique a formatação dos comentários no arquivo."
    )

def identificar_imports(codigo):
    imports = []

    try:
        arvore = ast.parse(codigo)
        nomes_usados = {
            no.id for no in ast.walk(arvore)
            if isinstance(no, ast.Name)
        }

        for no in ast.walk(arvore):
            if isinstance(no, ast.Attribute):
                raiz = no
                while isinstance(raiz, ast.Attribute):
                    raiz = raiz.value
                if isinstance(raiz, ast.Name):
                    nomes_usados.add(raiz.id)

    except SyntaxError:
        # Fallback caso haja erro de sintaxe/indentação no trecho da questão
        nomes_usados = set()
        for biblioteca in BIBLIOTECAS:
            if re.search(rf"\b{biblioteca}\b", codigo):
                nomes_usados.add(biblioteca)

    for biblioteca, instrucao in BIBLIOTECAS.items():
        if biblioteca in nomes_usados:
            imports.append(instrucao)

    return imports

questoes = {}

for i, marcador in enumerate(marcadores):
    numero = int(marcador.group(1))

    # Pula a linha do comentário do marcador para não incluir o título dentro do código final
    inicio = conteudo.find("\n", marcador.start())
    if inicio == -1:
        inicio = marcador.end()
    else:
        inicio += 1

    fim = (
        marcadores[i + 1].start()
        if i + 1 < len(marcadores)
        else len(conteudo)
    )

    codigo = conteudo[inicio:fim].strip()

    if codigo:
        questoes[numero] = codigo

# Salva cada questão em seu respectivo arquivo .py
for numero, codigo in questoes.items():
    imports = identificar_imports(codigo)

    if imports:
        codigo_final = "\n".join(imports) + "\n\n" + codigo + "\n"
    else:
        codigo_final = codigo + "\n"

    destino = pasta_saida / f"questao_{numero:02d}.py"
    destino.write_text(codigo_final, encoding="utf-8")

    print(f"Criado: {destino.name}")

print("\nSeparação concluída!")
print(f"Total de questões encontradas: {len(questoes)}")
print(f"Arquivos salvos em: {pasta_saida.resolve()}")

# Verificação de cobertura (1 a 80)
esperadas = set(range(1, 81))
encontradas = set(questoes.keys())
faltantes = sorted(esperadas - encontradas)

if faltantes:
    print("Questões sem marcador encontrado:", faltantes)
else:
    print("Todas as 80 questões foram encontradas e processadas com sucesso!")