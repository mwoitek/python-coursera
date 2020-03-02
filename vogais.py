def vogal(caractere):
    vog_mai = [65, 69, 73, 79, 85]
    vog_min = [i + 32 for i in vog_mai]
    vogais1 = vog_mai + vog_min
    vogais2 = [chr(i) for i in vogais1]
    eh_vogal = False
    for vog in vogais2:
        if (vog == caractere):
            eh_vogal = True
            break
    return eh_vogal
