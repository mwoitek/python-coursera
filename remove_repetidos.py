def remove_repetidos(lista):
    maior = lista[0]
    for i in range(1, len(lista)):
        if (lista[i] > maior):
            maior = lista[i]
    conta = (maior + 1) * [0]
    for elem in lista:
        conta[elem] += 1
    lista_ord = []
    for i in range(maior + 1):
        if (conta[i] != 0):
            lista_ord.append(i)
    return lista_ord
