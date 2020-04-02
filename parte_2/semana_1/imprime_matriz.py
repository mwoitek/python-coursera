def imprime_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    for i in range(linhas):
        linha = ""
        for j in range(colunas):
            linha += str(matriz[i][j]) + " "
        print(linha.strip())

#minha_matriz = [[1], [2], [3]]
#imprime_matriz(minha_matriz)
#minha_matriz = [[1, 2, 3], [4, 5, 6]]
#imprime_matriz(minha_matriz)
