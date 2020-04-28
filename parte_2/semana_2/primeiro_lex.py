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
Solução para o segundo problema opcional da semana 2.
"""


def primeiro_lex(lista):
    """

    Função que recebe uma lista de strings e devolve a primeira string de
    acordo com a ordem lexicográfica.

    Argumento:
      lista: Lista de strings.

    Retorna:
      Esta função retorna a primeira string na lista especificada (de acordo
      com a ordem lexicográfica).

    """

    if len(lista) == 1:
        return lista[0]
    else:
        aux = primeiro_lex(lista[1:])
        if lista[0] < aux:
            return lista[0]
        else:
            return aux
