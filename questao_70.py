def buscarPermissao(perfis, perfil, indice):
    try:
        return perfis[perfil][indice]
    except (KeyError, IndexError):
        return "acesso_restrito"
