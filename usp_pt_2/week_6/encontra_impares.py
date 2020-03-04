def encontra_impares(lista):
    if lista == []:
        return []
    else:
        x = lista.pop(0)
        y = [] if x % 2 == 0 else [x]
        return y + encontra_impares(lista)
