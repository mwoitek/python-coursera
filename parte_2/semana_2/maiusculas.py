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
Solução para o primeiro problema obrigatório da semana 2.
"""


# Cria uma lista com as letras maiúsculas. Caracteres especiais também serão
# incluídos.
letras = [chr(i) for i in range(65, 91)]
temp = [192, 193, 194, 195, 199, 201, 202, 205, 211, 212, 213, 218]
for i in temp:
    letras.append(chr(i))


def maiusculas(frase):
    """

    Argumento:
      frase: String que corresponde a uma frase.

    Retorna:
      Esta função retorna uma string com as letras maiúsculas que existem na
      frase especificada. Essas letras são devolvidas na ordem em que elas
      aparecem originalmente.

    """

    global letras

    temp = []
    for carac in frase:
        if carac in letras:
            temp.append(carac)

    return "".join(temp)
