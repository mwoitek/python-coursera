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
Implementação do algoritmo de busca binária.
"""


from math import floor


def busca(lista, elemento):
    """

    Função que realiza buscas em listas usando o algoritmo de busca binária.

    Argumentos:
      lista:    Lista onde vamos procurar um elemento.
      elemento: Elemento que procuramos na lista.

    Retorna:
      Esta função busca o elemento especificado na lista informada.
      Se esse elemento for encontrado, a função devolve o índice
      que corresponde à posição do elemento.
      Se ele não for encontrado, a função devolve False.

    """

    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:

        # floor(x) retorna o maior número inteiro menor ou igual a x.
        # A implementação do algoritmo não exige o comando print abaixo.
        # Ele só foi adicionado porque o enunciado do problema pede.
        meio = floor((esquerda + direita) / 2)
        print(meio)

        if lista[meio] < elemento:
            esquerda = meio + 1
        elif lista[meio] > elemento:
            direita = meio - 1
        else:
            return meio

    return False
