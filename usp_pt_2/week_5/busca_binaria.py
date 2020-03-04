from math import floor

def busca(lista, elemento):
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        m = floor((esquerda + direita) / 2)
        print(m)
        if lista[m] < elemento:
            esquerda = m + 1
        elif lista[m] > elemento:
            direita = m - 1
        else:
            return m
    return False
