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
Módulo para testar a implementação do algoritmo de BUSCA SEQUENCIAL.
"""


# Importa o módulo que desejamos testar.
import busca_sequencial as bs


def test_busca_sequencial():

    # Testa a 1ª versão do algoritmo.
    assert bs.busca(["a", "e", "i"], "a") == 0
    assert bs.busca(["a", "e", "i"], "e") == 1
    assert bs.busca(["a", "e", "i"], "i") == 2
    assert bs.busca(["a", "e", "i"], "o") == False
    assert bs.busca([1, 2, 3, 4, 5], 1) == 0
    assert bs.busca([1, 2, 3, 4, 5], 2) == 1
    assert bs.busca([1, 2, 3, 4, 5], 3) == 2
    assert bs.busca([1, 2, 3, 4, 5], 4) == 3
    assert bs.busca([1, 2, 3, 4, 5], 5) == 4
    assert bs.busca([1, 2, 3, 4, 5], 6) == False

    # Testa a 2ª versão do algoritmo.
    assert bs.busca_sentinela(["a", "e", "i"], "a") == 0
    assert bs.busca_sentinela(["a", "e", "i"], "e") == 1
    assert bs.busca_sentinela(["a", "e", "i"], "i") == 2
    assert bs.busca_sentinela(["a", "e", "i"], "o") == False
    assert bs.busca_sentinela([1, 2, 3, 4, 5], 1) == 0
    assert bs.busca_sentinela([1, 2, 3, 4, 5], 2) == 1
    assert bs.busca_sentinela([1, 2, 3, 4, 5], 3) == 2
    assert bs.busca_sentinela([1, 2, 3, 4, 5], 4) == 3
    assert bs.busca_sentinela([1, 2, 3, 4, 5], 5) == 4
    assert bs.busca_sentinela([1, 2, 3, 4, 5], 6) == False

    # Testa a 3ª versão do algoritmo.
    assert bs.busca_ordem(["a", "e", "i"], "a") == 0
    assert bs.busca_ordem(["a", "e", "i"], "e") == 1
    assert bs.busca_ordem(["a", "e", "i"], "i") == 2
    assert bs.busca_ordem(["a", "e", "i"], "o") == False
    assert bs.busca_ordem([1, 2, 3, 4, 5], 1) == 0
    assert bs.busca_ordem([1, 2, 3, 4, 5], 2) == 1
    assert bs.busca_ordem([1, 2, 3, 4, 5], 3) == 2
    assert bs.busca_ordem([1, 2, 3, 4, 5], 4) == 3
    assert bs.busca_ordem([1, 2, 3, 4, 5], 5) == 4
    assert bs.busca_ordem([1, 2, 3, 4, 5], 6) == False
