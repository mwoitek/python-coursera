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
Módulo que testa a solução para o primeiro problema opcional da semana 6.
"""


# Importa o módulo que desejamos testar.
import fibonacci_recursivo as fib


def test_fibonacci():

    assert fib.fibonacci(0) == 0
    assert fib.fibonacci(1) == 1
    assert fib.fibonacci(2) == 1
    assert fib.fibonacci(3) == 2
    assert fib.fibonacci(4) == 3
    assert fib.fibonacci(5) == 5
    assert fib.fibonacci(6) == 8
    assert fib.fibonacci(7) == 13
    assert fib.fibonacci(8) == 21
    assert fib.fibonacci(9) == 34
    assert fib.fibonacci(10) == 55
    assert fib.fibonacci(11) == 89
    assert fib.fibonacci(12) == 144
    assert fib.fibonacci(13) == 233
    assert fib.fibonacci(14) == 377
    assert fib.fibonacci(15) == 610
    assert fib.fibonacci(16) == 987
    assert fib.fibonacci(17) == 1597
    assert fib.fibonacci(18) == 2584
    assert fib.fibonacci(19) == 4181
    assert fib.fibonacci(20) == 6765
