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
Módulo que testa a implementação do algoritmo de ordenação SELECTION SORT. Para
rodar este módulo, você precisa ter o pytest instalado na sua máquina.
"""


# Importa o módulo que desejamos testar.
import selection_sort as ssort


def test_selection_sort():

    assert ssort.ordena([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert ssort.ordena([1, 2, 3, 5, 4]) == [1, 2, 3, 4, 5]
    assert ssort.ordena([1, 2, 5, 4, 3]) == [1, 2, 3, 4, 5]
    assert ssort.ordena([1, 5, 4, 3, 2]) == [1, 2, 3, 4, 5]
    assert ssort.ordena([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert ssort.ordena([1, 2, 3, 4, 1]) == [1, 1, 2, 3, 4]
    assert ssort.ordena([1, 2, 0, 0, 0]) == [0, 0, 0, 1, 2]
    assert ssort.ordena([1, 2, 1, 2, 3]) == [1, 1, 2, 2, 3]
    assert ssort.ordena([1, 5, 4, 4, 4]) == [1, 4, 4, 4, 5]
    assert ssort.ordena([5, 5, 5, 5, 1]) == [1, 5, 5, 5, 5]
    assert ssort.ordena([1, 4, 3, 7, 9]) == [1, 3, 4, 7, 9]
    assert ssort.ordena([9, 8, 7, 6, 5]) == [5, 6, 7, 8, 9]
    assert ssort.ordena([0, 7, 6, 5, 8]) == [0, 5, 6, 7, 8]
    assert ssort.ordena([-1, -2, -3, 0]) == [-3, -2, -1, 0]
    assert ssort.ordena([6, -3, -9, -7]) == [-9, -7, -3, 6]
