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
Módulo que testa a solução para o primeiro problema opcional da semana 2.
"""


# Importa o módulo que desejamos testar.
import conta_char as cc


def test_conta_char():

    assert cc.conta_letras("Isso é um teste!") == 6
    assert cc.conta_letras("Isso é um teste!", "vogais") == 6
    assert cc.conta_letras("Isso é um teste!", "consoantes") == 6
    assert cc.conta_letras("Eu estou usando o pytest.") == 10
    assert cc.conta_letras("Eu estou usando o pytest.", "vogais") == 10
    assert cc.conta_letras("Eu estou usando o pytest.", "consoantes") == 10
    assert cc.conta_letras("O José é filho do João.") == 10
    assert cc.conta_letras("O José é filho do João.", "vogais") == 10
    assert cc.conta_letras("O José é filho do João.", "consoantes") == 7
    assert cc.conta_letras("Esse é um exercício de programação!") == 15
    assert cc.conta_letras("Esse é um exercício de programação!", "vogais") == 15
    assert cc.conta_letras("Esse é um exercício de programação!", "consoantes") == 14
    assert cc.conta_letras("programamos em python") == 6
    assert cc.conta_letras("programamos em python", "vogais") == 6
    assert cc.conta_letras("programamos em python", "consoantes") == 13
