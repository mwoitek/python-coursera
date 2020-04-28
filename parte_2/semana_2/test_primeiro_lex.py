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
Módulo que testa a solução para o segundo problema opcional da semana 2.
"""


# Importa o módulo que desejamos testar.
import primeiro_lex as pl


def test_primeiro_lex():

    assert pl.primeiro_lex(["aac", "aab", "abc", "acb"]) == "aab"
    assert pl.primeiro_lex(["aac", "aab", "ABC", "acb"]) == "ABC"
    assert pl.primeiro_lex(["a", "b", "c", "Z"]) == "Z"
    assert pl.primeiro_lex(["olá", "A", "a", "casa"]) == "A"
    assert pl.primeiro_lex(["Olá", "a", "casa"]) == "Olá"
    assert pl.primeiro_lex(["Olá", "a", "Casa"]) == "Casa"
    assert pl.primeiro_lex(["AAAAAA", "b"]) == "AAAAAA"
    assert pl.primeiro_lex(["aaaaaa", "B"]) == "B"
