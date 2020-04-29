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
Módulo que testa a solução para o primeiro problema obrigatório da semana 6.
"""


# Importa o módulo que desejamos testar.
import soma_lista_recursivo as slr


def test_soma_lista():

    assert slr.soma_lista([1, 2, 3, 4]) == 10
    assert slr.soma_lista([-1, 0, 1, 2]) == 2
    assert slr.soma_lista([5, 6, 7]) == 18
    assert slr.soma_lista([-3, -2, -1]) == -6
    assert slr.soma_lista([4, 4, 4, 4]) == 16
    assert slr.soma_lista([5]) == 5
    assert slr.soma_lista([]) == 0
