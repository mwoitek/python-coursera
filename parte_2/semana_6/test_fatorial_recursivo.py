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
Módulo que testa a solução para o segundo problema opcional da semana 6.
"""


# Importa o módulo que desejamos testar.
import fatorial_recursivo as fr


def test_fatorial():

    assert fr.fatorial(0) == 1
    assert fr.fatorial(1) == 1
    assert fr.fatorial(2) == 2
    assert fr.fatorial(3) == 6
    assert fr.fatorial(4) == 24
    assert fr.fatorial(5) == 120
    assert fr.fatorial(6) == 720
    assert fr.fatorial(7) == 5040
    assert fr.fatorial(8) == 40320
    assert fr.fatorial(9) == 362880
    assert fr.fatorial(10) == 3628800
    assert fr.fatorial(11) == 39916800
    assert fr.fatorial(12) == 479001600
    assert fr.fatorial(13) == 6227020800
    assert fr.fatorial(14) == 87178291200
    assert fr.fatorial(15) == 1307674368000
