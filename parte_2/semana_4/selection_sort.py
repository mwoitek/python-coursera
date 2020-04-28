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
Implementação do algoritmo de ordenação SELECTION SORT.
"""


def ordena(lista):
    """

    Função que ordena uma lista de números inteiros usando o algoritmo de
    ordenação SELECTION SORT.

    Argumento:
      lista: Lista que desejamos ordenar.

    Retorna:
      Esta função devolve a lista especificada com os números em ORDEM
      CRESCENTE.

    """

    n = len(lista)

    # Loop que move a fronteira da sub-lista desordenada.
    for i in range(n - 1):

        # Encontra o menor valor na sub-lista desordenada.
        ind_min = i
        for j in range(i + 1, n):
            if lista[j] < lista[ind_min]:
                ind_min = j

        # Coloca o valor encontrado na sua devida posição.
        lista[i], lista[ind_min] = lista[ind_min], lista[i]

    return lista
