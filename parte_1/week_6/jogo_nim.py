"""
Implementação do jogo NIM.
"""


def computador_escolhe_jogada(n, m):
    """
    Função que recebe os inteiros n e m
    e devolve um inteiro correspondente
    à próxima jogada do computador.

    Argumentos:
      n: Número de peças na mesa.
      m: Número máximo de peças que podem ser retiradas de uma vez só.

    Retorna:
      Um inteiro correspondente à próxima jogada do computador.
      Ele utiliza a estratégia vencedora.
    """

    # Tenta encontrar o maior múltiplo de m + 1
    # que é estritamente menor do que n.
    achou = False
    m1 = m + 1
    mult = n - 1
    n1 = n - m1
    while (mult > n1):
        if (mult % m1 == 0):
            achou = True
            break
        else:
            mult -= 1

    # Escolhe a próxima jogada do computador.
    # Essa escolha depende do resultado da busca realizada acima.
    if (achou == True):
        jogada = n - mult
    elif (n >= m):
        jogada = m
    else:
        jogada = n

    return jogada


def usuario_escolhe_jogada(n, m):
    """
    Função que recebe os inteiros n e m.
    Depois ela solicita que o usuário informe a sua jogada
    e verifica se o valor informado é válido.
    Se ele for válido, a função devolve esse valor.
    Do contrário, a função solicita novamente
    que o usuário informe a sua jogada.

    Argumentos:
      n: Número de peças na mesa.
      m: Número máximo de peças que podem ser retiradas de uma vez só.

    Retorna:
      Um inteiro correspondente à próxima jogada do usuário.
      Um valor é retornado somente quando
      ele está relacionado com uma jogada válida.
    """

    # Lê a jogada do usuário.
    # A execução só continua se o usuário informar uma jogada válida.
    vale = False
    while (vale == False):
        jogada = int(input("Quantas peças você vai tirar? "))
        teste1 = jogada <= n
        teste2 = 1 <= jogada <= m
        if ((teste1 and teste2) == False):
            print("\nOops! Jogada inválida! Tente de novo.\n")
        else:
            vale = True
    print("")

    return jogada


def partida():
    """
    Esta função solicita que o usuário informe
    os valores de n e m e inicia o jogo.
    A cada jogada, a função imprime o estado atual do jogo.
    Quando a última peça for removida, esta função imprime
    'O computador ganhou!' ou 'Você ganhou!'.
    """

    global res

    # Solicita que o usuário informe os valores de n e m.
    vale = False
    while (vale == False):
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        if (n < 1):
            print("\nO número de peças não pode ser menor do que 1!")
            print("Tente novamente.\n")
        elif (m < 1):
            print("\nO limite não pode ser menor do que 1!")
            print("Tente novamente.\n")
        else:
            vale = True
    print("")

    # Início do jogo.

    # Decide se o primeiro a jogar é o usuário ou o computador.
    # A variável booleana usu_prim vai nos dizer
    # se o primeiro jogador é o usuário.
    if (n % (m + 1) == 0):
        usu_prim = True
        print("Você começa!\n")
    else:
        usu_prim = False
        print("Computador começa!\n")

    # Escolhe a maneira correta de alternar as jogadas.
    if (usu_prim == True):

        # Usuário joga e computador joga.
        while (n > 0):

            # Usuário joga.
            jogada = usuario_escolhe_jogada(n, m)
            if (jogada == 1):
                print("Você tirou uma peça.")
            else:
                print("Você tirou {:d} peças.".format(jogada))
            n -= jogada
            if (n == 0):
                res = "Você ganhou!"
                print("Fim do jogo! " + res + "\n")
                break
            elif (n == 1):
                print("Agora resta apenas uma peça no tabuleiro.\n")
            else:
                print("Agora restam {:d} peças no tabuleiro.\n".format(n))

            # Computador joga.
            jogada = computador_escolhe_jogada(n, m)
            if (jogada == 1):
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou {:d} peças.".format(jogada))
            n -= jogada
            if (n == 0):
                res = "O computador ganhou!"
                print("Fim do jogo! " + res + "\n")
                break
            elif (n == 1):
                print("Agora resta apenas uma peça no tabuleiro.\n")
            else:
                print("Agora restam {:d} peças no tabuleiro.\n".format(n))

    else:

        # Computador joga e usuário joga.
        while (n > 0):

            # Computador joga.
            jogada = computador_escolhe_jogada(n, m)
            if (jogada == 1):
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou {:d} peças.".format(jogada))
            n -= jogada
            if (n == 0):
                res = "O computador ganhou!"
                print("Fim do jogo! " + res + "\n")
                break
            elif (n == 1):
                print("Agora resta apenas uma peça no tabuleiro.\n")
            else:
                print("Agora restam {:d} peças no tabuleiro.\n".format(n))

            # Usuário joga.
            jogada = usuario_escolhe_jogada(n, m)
            if (jogada == 1):
                print("Você tirou uma peça.")
            else:
                print("Você tirou {:d} peças.".format(jogada))
            n -= jogada
            if (n == 0):
                res = "Você ganhou!"
                print("Fim do jogo! " + res + "\n")
                break
            elif (n == 1):
                print("Agora resta apenas uma peça no tabuleiro.\n")
            else:
                print("Agora restam {:d} peças no tabuleiro.\n".format(n))


def campeonato():
    """
    Esta função realiza 3 partidas do jogo.
    No final, a função imprime o placar que corresponde a essas 3 partidas.
    Ela também indica o vencedor do campeonato.
    """

    global res

    # Número de partidas em que o usuário foi o vencedor.
    usu_ganhou = 0

    # Loop que realiza as 3 partidas.
    for i in range(3):
        print("**** Rodada {:d} ****\n".format(i + 1))
        partida()
        if (res == "Você ganhou!"):
            usu_ganhou += 1
    print("**** Final do campeonato! ****\n")

    # Imprime o placar.
    placar = "Placar: Você {:d} X {:d} Computador\n"
    print(placar.format(usu_ganhou, 3 - usu_ganhou))


def main():

    print("\nBem-vindo ao jogo do NIM! Escolha:\n")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato\n")

    # Lê a opção do usuário.
    # A execução só continua se o usuário escolher uma opção válida.
    vale = False
    while (vale == False):
        opc = input()
        if ((opc != "1") and (opc != "2")):
            print("\nA opção escolhida não existe! Tente novamente!\n")
        else:
            vale = True
    print("")

    # Partida ou campeonato?
    if (opc == "1"): # Partida
        print("Você escolheu uma partida!\n")
        partida()
    else: # Campeonato
        print("Você escolheu um campeonato!\n")
        campeonato()


main()
