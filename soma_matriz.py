def dimensoes(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    return [linhas, colunas]

def soma_matrizes(m1, m2):
    dim_m1 = dimensoes(m1)
    dim_m2 = dimensoes(m2)
    if dim_m1 != dim_m2:
        return False
    else:
        soma = []
        for i in range(dim_m1[0]):
            soma.append([m1[i][j] + m2[i][j] for j in range(dim_m1[1])])
        return soma
