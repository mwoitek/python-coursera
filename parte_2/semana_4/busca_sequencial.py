def busca(lista, elemento):
    i = 0
    tam = len(lista)
    while i < tam and lista[i] != elemento:
        i += 1
    return False if i == tam else i
