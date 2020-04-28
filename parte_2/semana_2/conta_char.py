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
Solução para o primeiro problema opcional da semana 2.
"""


# Cria uma lista com todas as consoantes.
cons_minus = ["ç"]
for i in range(98, 123):
    if i not in [101, 105, 111, 117]:
        cons_minus.append(chr(i))
cons_maius = []
for cons in cons_minus:
    cons_maius.append(cons.upper())
consoantes = cons_minus + cons_maius

# Cria uma lista com todas as vogais. Caracteres especiais também serão
# incluídos.
vogais_minus = ["a", "e", "i", "o", "u", "à", "á", "â",
                "ã", "é", "ê", "í", "ó", "ô", "õ", "ú"]
vogais_maius = []
for vogal in vogais_minus:
    vogais_maius.append(vogal.upper())
vogais = vogais_minus + vogais_maius


def conta_letras(frase, contar="vogais"):
    """

    Função que recebe uma string com uma frase e devolve o número de vogais ou
    consoantes nessa frase.

    Argumentos:
      frase:  String com uma frase.
      contar: String para indicar se a função deve contar vogais ou consoantes.

    Retorna:
      Esta função retorna a quantidade de vogais ou consoantes na frase
      especificada.

    """

    global consoantes
    global vogais

    # Verifica se a função deve contar vogais ou consoantes.
    if contar == "vogais":
        tipo = vogais
    elif contar == "consoantes":
        tipo = consoantes
    else:
        return 0

    # Loop que determina a quantidade de vogais ou consoantes na frase
    # especificada.
    numero = 0
    for carac in frase:
        if carac in tipo:
            numero += 1

    return numero
