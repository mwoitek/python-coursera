def bubble_sort(lista):
    tam = len(lista)
    for i in range(tam - 1):
        trocou = False
        for j in range(tam - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
                print(lista)
        if not trocou:
            break
    return lista
