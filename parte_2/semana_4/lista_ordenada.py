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
Solução para o primeiro problema obrigatório da semana 4.
"""


def ordenada(lista):
    """

    Função que determina se uma lista de números inteiros está ordenada.

    Argumento:
      lista: Lista de números inteiros.

    Retorna:
      Quando a lista especificada está ordenada, a função devolve True. Do
      contrário, ela retorna False.

    """

    tam = len(lista)

    # Inicialmente, assume-se que a lista especificada está ordenada.
    em_ordem = True

    i = 0
    while em_ordem and i < tam - 1:
        for j in range(i + 1, tam):
            # Verifica se os elementos da lista estão em ORDEM CRESCENTE.
            if lista[i] > lista[j]:
                em_ordem = False
                break
        i += 1

    return em_ordem
