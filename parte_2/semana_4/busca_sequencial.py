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
Implementação do algoritmo de BUSCA SEQUENCIAL.
"""


def busca(lista, elemento):
    """

    Função que realiza buscas em listas usando o algoritmo de BUSCA SEQUENCIAL.

    Argumentos:
      lista:    Lista onde vamos procurar um elemento.
      elemento: Elemento que procuramos na lista.

    Retorna:
      Esta função busca o elemento especificado na lista informada. Se esse
      elemento for encontrado, a função devolve o índice que corresponde à
      posição do elemento. Se ele não for encontrado, a função devolve False.

    """

    tam = len(lista)
    i = 0
    while i < tam and lista[i] != elemento:
        i += 1

    return False if i == tam else i


# O código que segue é DESNECESSÁRIO. As duas funções abaixo são VERSÕES
# ALTERNATIVAS do algoritmo de BUSCA SEQUENCIAL.


def busca_sentinela(lista, elemento):
    """

    Função que realiza buscas em listas usando o algoritmo de BUSCA SEQUENCIAL.
    Esta versão do algoritmo utiliza uma SENTINELA IGUAL ao elemento procurado.

    Argumentos:
      lista:    Lista onde vamos procurar um elemento.
      elemento: Elemento que procuramos na lista.

    Retorna:
      Esta função busca o elemento especificado na lista informada. Se esse
      elemento for encontrado, a função devolve o índice que corresponde à
      posição do elemento. Se ele não for encontrado, a função devolve False.

    """

    # Adiciona à lista a SENTINELA.
    lista.append(elemento)

    i = 0
    while lista[i] != elemento:
        i += 1

    # Se o índice i tiver o maior valor possível, então o algoritmo encontrou a
    # sentinela. Isso significa que o elemento procurado não está na lista
    # original.
    return False if i == len(lista) - 1 else i


def busca_ordem(lista, elemento):
    """

    Função que realiza buscas em listas usando o algoritmo de BUSCA SEQUENCIAL.
    Para realizar uma busca, primeiro esta versão do algoritmo coloca a lista
    especificada EM ORDEM. Além disso, esta implementação utiliza uma SENTINELA
    MAIOR do que o elemento procurado.

    Argumentos:
      lista:    Lista onde vamos procurar um elemento.
      elemento: Elemento que procuramos na lista.

    Retorna:
      Esta função busca o elemento especificado na lista informada. Se esse
      elemento for encontrado, a função devolve o índice que corresponde à
      posição do elemento. Se ele não for encontrado, a função devolve False.

    """

    lista.sort()

    # Adiciona à lista a SENTINELA. A escolha da sentinela depende do tipo de
    # dado do elemento procurado.
    sentinela = "~" if type(elemento) is str else elemento + 1
    lista.append(sentinela)

    i = 0
    while lista[i] < elemento:
        i += 1

    # Como a lista está ordenada, se o elemento na posição i for maior do que o
    # procurado, então o elemento que buscamos não está na lista.
    return False if lista[i] > elemento else i
