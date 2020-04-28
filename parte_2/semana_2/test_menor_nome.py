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
Módulo que testa a solução para o segundo problema obrigatório da semana 2.
"""


# Importa o módulo que desejamos testar.
import menor_nome as mn


def test_menor_nome():

    assert mn.menor_nome(["  marcos ", "ANA", "Fernanda "]) == "Ana"
    assert mn.menor_nome(["FERNANDO", "   carolina  ", " beto", "Mário"]) == "Beto"
    assert mn.menor_nome([" CarlA   ", "RODRIGO", "Diego", " mariana "]) == "Carla"
    assert mn.menor_nome(["   DaVi  ", "JAIR", "Beto"]) == "Davi"
    assert mn.menor_nome(["  gilberto ", " eNZO   ", " júlia   ", "Pedro"]) == "Enzo"
    assert mn.menor_nome([" rOBERTo   ", " Juliana", "FÁBIO", "alice"]) == "Fábio"
    assert mn.menor_nome(["HUgo    ", " Fátima ", "FABIANA"]) == "Hugo"
    assert mn.menor_nome(["maria", "josé", "PAULO", "Catarina"]) == "José"
    assert mn.menor_nome(["maria", " josé  ", "  PAULO", "Catarina  "]) == "José"
    assert mn.menor_nome(["Bárbara", "JOSÉ  ", "Bill"]) == "José"
