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
Módulo que testa a solução para o primeiro problema obrigatório da semana 2.
"""


# Importa o módulo que desejamos testar.
import maiusculas


def test_maiusculas():

    assert maiusculas.maiusculas("Ângela mora no Rio de Janeiro.") == "ÂRJ"
    assert maiusculas.maiusculas("Eu me interesso por PROGRAMAÇÃO!") == "EPROGRAMAÇÃO"
    assert maiusculas.maiusculas("O meu NOME é JOSÉ.") == "ONOMEJOSÉ"
    assert maiusculas.maiusculas("Érica, ANTÔNIO, JÚLIA, Mário") == "ÉANTÔNIOJÚLIAM"
    assert maiusculas.maiusculas("Úrsula nasceu em Belo Horizonte.") == "ÚBH"
    assert maiusculas.maiusculas("Eu moro em Porto Alegre.") == "EPA"
    assert maiusculas.maiusculas("Ele se chama Renato.") == "ER"
    assert maiusculas.maiusculas("Estou realizando um teste.") == "E"
    assert maiusculas.maiusculas("A filha da Maria se chama Ana.") == "AMA"
    assert maiusculas.maiusculas("A Ana tem dois filhos, Jair e Pedro.") == "AAJP"
    assert maiusculas.maiusculas("Buenos Aires fica na Argentina.") == "BAA"
    assert maiusculas.maiusculas("EU ESTOU USANDO O PYTEST!") == "EUESTOUUSANDOOPYTEST"
    assert maiusculas.maiusculas("Programamos em python 2?") == "P"
    assert maiusculas.maiusculas("Programamos em Python 3.") == "PP"
    assert maiusculas.maiusculas("PrOgRaMaMoS em python!") == "PORMMS"
