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
Módulo que testa a solução para o terceiro problema obrigatório da semana 6.
"""


# Importa o módulo que desejamos testar.
import elefantes as el


def test_incomodam():

    assert el.incomodam(-1) == ""
    assert el.incomodam(0) == ""
    assert el.incomodam(1) == "incomodam "
    assert el.incomodam(2) == "incomodam incomodam "
    assert el.incomodam(3) == "incomodam incomodam incomodam "


def test_elefantes():

    assert el.elefantes(-1) == ""
    assert el.elefantes(0) == ""
    assert el.elefantes(1) == ""
    assert el.elefantes(2) == "Um elefante incomoda muita gente\n2 elefantes incomodam incomodam muito mais"
    assert el.elefantes(3) == "Um elefante incomoda muita gente\n2 elefantes incomodam incomodam muito mais\n2 elefantes incomodam muita gente\n3 elefantes incomodam incomodam incomodam muito mais"
    assert el.elefantes(4) == "Um elefante incomoda muita gente\n2 elefantes incomodam incomodam muito mais\n2 elefantes incomodam muita gente\n3 elefantes incomodam incomodam incomodam muito mais\n3 elefantes incomodam muita gente\n4 elefantes incomodam incomodam incomodam incomodam muito mais"
