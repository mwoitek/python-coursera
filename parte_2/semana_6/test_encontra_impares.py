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
Módulo que testa a solução para o segundo problema obrigatório da semana 6.
"""


# Importa o módulo que desejamos testar.
import encontra_impares as ei


def test_encontra_impares():

    assert ei.encontra_impares([1, 3, 5]) == [1, 3, 5]
    assert ei.encontra_impares([2, 4, 6]) == []
    assert ei.encontra_impares([1, 2, 3, 4, 5]) == [1, 3, 5]
    assert ei.encontra_impares([2, 4, 6, 7]) == [7]
    assert ei.encontra_impares([]) == []
    assert ei.encontra_impares([1, 1, 1, 2]) == [1, 1, 1]
    assert ei.encontra_impares([4, 8, 9, 5, 7, 10]) == [9, 5, 7]
    assert ei.encontra_impares([6, 0, 1, 3, 2, 11]) == [1, 3, 11]
    assert ei.encontra_impares([4, 8, 12, 6, 14, 10]) == []
    assert ei.encontra_impares([7, 9, 11, 3, 5, 21]) == [7, 9, 11, 3, 5, 21]
