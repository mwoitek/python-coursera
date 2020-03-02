def maiusculas(frase):
    aux = []
    letras = [chr(i) for i in range(65, 91)]
    for carac in frase:
        for letra in letras:
            if carac == letra:
                aux.append(carac)
    return "".join(aux)
