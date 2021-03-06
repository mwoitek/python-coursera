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
Implementação do algoritmo de ordenação BUBBLE SORT.
"""


def bubble_sort(lista):
    """

    Função que ordena uma lista de números inteiros
    usando o algoritmo de ordenação BUBBLE SORT.

    Argumento:
      lista: Lista que desejamos ordenar.

    Retorna:
      Esta função devolve a lista especificada
      com os números em ordem crescente.

    """

    n = len(lista)
    while n > 1:
        novo_n = 0
        for i in range(1, n):
            if lista[i - 1] > lista[i]:
                lista[i - 1], lista[i] = lista[i], lista[i - 1]
                novo_n = i
                # O comando abaixo não é parte do algoritmo.
                # Ele só foi adicionado porque o enunciado do problema pede.
                print(lista)
        n = novo_n

    return lista
