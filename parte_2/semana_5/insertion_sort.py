#!/usr/bin/env python3
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
Implementação do algoritmo de ordenação INSERTION SORT.
"""


def insertion_sort(lista):
    """

    Função que ordena uma lista de números inteiros
    usando o algoritmo de ordenação INSERTION SORT.

    Argumento:
      lista: Lista que desejamos ordenar.

    Retorna:
      Esta função devolve a lista especificada
      com os números em ordem crescente.

    """

    i = 1

    while i < len(lista):

        temp = lista[i]
        j = i - 1

        while ((j >= 0) and (lista[j] > temp)):
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = temp
        i += 1

    return lista
