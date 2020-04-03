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
Módulo para testar a solução para o
problema de determinar se uma lista está ordenada.
"""


# Importa o módulo que desejamos testar.
import lista_ordenada as lo


def test_lista_ordenada():
    assert lo.ordenada([1, 2, 3, 4, 9]) == True
    assert lo.ordenada([1, 2, 3, 4, 0]) == False
    assert lo.ordenada([1, 3, 5, 7, 9]) == True
    assert lo.ordenada([5, 6, 7, 2, 9]) == False
    assert lo.ordenada([1, 2, 3, 4, 5]) == True
    assert lo.ordenada([1, 2, 3, 5, 4]) == False
    assert lo.ordenada([1, 2, 5, 6, 8]) == True
    assert lo.ordenada([1, 5, 4, 3, 2]) == False
    assert lo.ordenada([1, 2, 3, 4, 4]) == True
    assert lo.ordenada([5, 4, 3, 2, 1]) == False
    assert lo.ordenada([1, 2, 6, 6, 6]) == True
    assert lo.ordenada([1, 2, 1, 2, 3]) == False
    assert lo.ordenada([5, 5, 5, 5, 7]) == True
    assert lo.ordenada([1, 5, 4, 4, 4]) == False
    assert lo.ordenada([1, 4, 6, 7, 9]) == True
    assert lo.ordenada([9, 8, 7, 6, 5]) == False
    assert lo.ordenada([-3, -2, -1, 0]) == True
    assert lo.ordenada([0, 7, 6, 5, 8]) == False
