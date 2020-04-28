#
#
#
# ██╗    ██╗ ██████╗ ██╗████████╗███████╗██╗  ██╗
# ██║    ██║██╔═══██╗██║╚══██╔══╝██╔════╝██║ ██╔╝
# ██║ █╗ ██║██║   ██║██║   ██║   █████╗  █████╔╝
# ██║███╗██║██║   ██║██║   ██║   ██╔══╝  ██╔═██╗
# ╚███╔███╔╝╚██████╔╝██║   ██║   ███████╗██║  ██╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
#
#
#
#   ____        _   _
#  |  _ \ _   _| |_| |__   ___  _ __
#  | |_) | | | | __| '_ \ / _ \| '_ \
#  |  __/| |_| | |_| | | | (_) | | | |
#  |_|    \__, |\__|_| |_|\___/|_| |_|
#         |___/
#
#
#

"""
Solução para o segundo problema obrigatório da semana 2.
"""


def menor(inteiros):
    """

    Função que encontra recursivamente o menor número numa lista de inteiros.

    Argumento:
      inteiros: Lista de números inteiros.

    Retorna:
      Esta função retorna o menor número na lista especificada.

    """

    if len(inteiros) == 1:
        return inteiros[0]
    else:
        aux = menor(inteiros[1:])
        if inteiros[0] < aux:
            return inteiros[0]
        else:
            return aux


def menor_nome(nomes):
    """

    Função que recebe uma lista com nomes de pessoas e devolve o nome mais
    curto nessa lista.

    Argumento:
      nomes: Lista de strings com os nomes.

    Retorna:
      Esta função retorna o nome mais curto na lista especificada. Espaços
      antes e depois dos nomes são ignorados. O menor nome é devolvido com a
      primeira letra maiúscula e os outros caracteres minúsculos. Quando tem
      mais de um nome com o menor comprimento, esta função devolve apenas o
      primeiro.

    """

    nomes_strip = [nome.strip() for nome in nomes]
    nomes_len = [len(nome) for nome in nomes_strip]
    menor_len = menor(nomes_len)

    i = 0
    while nomes_len[i] != menor_len:
        i += 1

    return nomes_strip[i].lower().capitalize()
