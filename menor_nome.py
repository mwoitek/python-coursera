def menor(inteiros):
    if len(inteiros) == 2:
        if inteiros[0] < inteiros[1]:
            return inteiros[0]
        else:
            return inteiros[1]
    else:
        aux = menor(inteiros[1:])
        if inteiros[0] < aux:
            return inteiros[0]
        else:
            return aux

def menor_nome(nomes):
    nomes_lower = [nome.lower() for nome in nomes]
    nomes_strip = [nome.strip() for nome in nomes_lower]
    nomes_len = [len(nome) for nome in nomes_strip]
    menor_len = menor(nomes_len)
    testes = [i != menor_len for i in nomes_len]
    i = 0
    teste = testes[i]
    while teste:
        i += 1
        teste = testes[i]
    return nomes_strip[i].capitalize()
