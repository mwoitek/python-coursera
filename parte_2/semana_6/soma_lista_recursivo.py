def soma_lista(lista):
    if lista == []:
        return 0
    else:
        x = lista.pop(0)
        return x + soma_lista(lista)
