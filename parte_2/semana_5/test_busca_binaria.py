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
Módulo que testa a implementação do algoritmo de busca binária.
Para rodar este módulo, você precisa ter o pytest instalado na sua máquina.
"""


# Importa o módulo que desejamos testar.
import busca_binaria as bb


def test_busca_binaria():
    assert bb.busca(["a", "e", "i"], "a") == 0
    assert bb.busca(["a", "e", "i"], "e") == 1
    assert bb.busca(["a", "e", "i"], "i") == 2
    assert bb.busca(["a", "e", "i"], "o") == False
    assert bb.busca([1, 2, 3, 4, 5], 1) == 0
    assert bb.busca([1, 2, 3, 4, 5], 2) == 1
    assert bb.busca([1, 2, 3, 4, 5], 3) == 2
    assert bb.busca([1, 2, 3, 4, 5], 4) == 3
    assert bb.busca([1, 2, 3, 4, 5], 5) == 4
    assert bb.busca([1, 2, 3, 4, 5], 6) == False
