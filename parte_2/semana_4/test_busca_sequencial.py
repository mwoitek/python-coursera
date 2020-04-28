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
Módulo para testar a implementação do algoritmo de BUSCA SEQUENCIAL.
"""


# Importa o módulo que desejamos testar.
import busca_sequencial as bs


def um_algoritmo(funcao):

    assert funcao(["a", "e", "i"], "a") == 0
    assert funcao(["a", "e", "i"], "e") == 1
    assert funcao(["a", "e", "i"], "i") == 2
    assert funcao(["a", "e", "i"], "o") == False
    assert funcao([1, 2, 3, 4, 5], 1) == 0
    assert funcao([1, 2, 3, 4, 5], 2) == 1
    assert funcao([1, 2, 3, 4, 5], 3) == 2
    assert funcao([1, 2, 3, 4, 5], 4) == 3
    assert funcao([1, 2, 3, 4, 5], 5) == 4
    assert funcao([1, 2, 3, 4, 5], 6) == False


def test_busca_sequencial():

    # Testa a 1ª versão do algoritmo.
    um_algoritmo(bs.busca)

    # Testa a 2ª versão do algoritmo.
    um_algoritmo(bs.busca_sentinela)

    # Testa a 3ª versão do algoritmo.
    um_algoritmo(bs.busca_ordem)
