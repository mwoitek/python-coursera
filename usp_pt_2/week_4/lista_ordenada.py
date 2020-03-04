def ordenada(lista):
    em_ordem = True
    i = 0
    tam = len(lista)
    while i < tam - 1 and em_ordem:
        for j in range(i + 1, tam):
            if lista[i] > lista[j]:
                em_ordem = False
                break
        i += 1
    return em_ordem
