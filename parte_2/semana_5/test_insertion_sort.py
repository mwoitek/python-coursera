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
Módulo que testa a implementação do algoritmo de ordenação INSERTION SORT.
Para rodar este módulo, você precisa ter o pytest instalado na sua máquina.
"""


# Importa o módulo que desejamos testar.
import insertion_sort as isort


def test_insertion_sort():
    assert isort.insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert isort.insertion_sort([1, 2, 3, 5, 4]) == [1, 2, 3, 4, 5]
    assert isort.insertion_sort([1, 2, 5, 4, 3]) == [1, 2, 3, 4, 5]
    assert isort.insertion_sort([1, 5, 4, 3, 2]) == [1, 2, 3, 4, 5]
    assert isort.insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert isort.insertion_sort([1, 2, 3, 4, 1]) == [1, 1, 2, 3, 4]
    assert isort.insertion_sort([1, 2, 0, 0, 0]) == [0, 0, 0, 1, 2]
    assert isort.insertion_sort([1, 2, 1, 2, 3]) == [1, 1, 2, 2, 3]
    assert isort.insertion_sort([1, 5, 4, 4, 4]) == [1, 4, 4, 4, 5]
    assert isort.insertion_sort([5, 5, 5, 5, 1]) == [1, 5, 5, 5, 5]
    assert isort.insertion_sort([1, 4, 3, 7, 9]) == [1, 3, 4, 7, 9]
    assert isort.insertion_sort([9, 8, 7, 6, 5]) == [5, 6, 7, 8, 9]
    assert isort.insertion_sort([0, 7, 6, 5, 8]) == [0, 5, 6, 7, 8]
    assert isort.insertion_sort([-1, -2, -3, 0]) == [-3, -2, -1, 0]
    assert isort.insertion_sort([6, -3, -9, -7]) == [-9, -7, -3, 6]
