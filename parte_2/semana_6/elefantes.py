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
Solução para o terceiro problema obrigatório da semana 6.
"""


def incomodam(n):
    """

    Função que corresponde à solução para a primeira parte do problema.

    Argumento:
      n: Número inteiro.

    Retorna:
      Se n for estritamente positivo, esta função retorna uma string que contém
      'incomodam ' n vezes. Caso contrário, uma string vazia é devolvida.

    """

    if n < 1:
        return ""
    else:
        return "incomodam " + incomodam(n - 1)


def elefantes(n):
    """

    Função que corresponde à solução para a segunda parte do problema.

    Argumento:
      n: Número inteiro.

    Retorna:
      Se n for maior do que 1, esta função retorna uma string que contém a
      letra da música 'Um Elefante Incomoda Muita Gente'. Caso contrário, uma
      string vazia é devolvida.

    """

    if n < 2:
        return ""
    else:
        if n == 2:
            str1 = "Um elefante incomoda muita gente\n"
        else:
            str1 = "\n" + str(n - 1) + " elefantes incomodam muita gente\n"
        str2 = str(n) + " elefantes " + incomodam(n) + "muito mais"
        return elefantes(n - 1) + str1 + str2
