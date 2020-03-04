from matriz_mult import *

def test_matriz_mult():
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[2, 3, 4], [5, 6, 7]]
    assert sao_multiplicaveis(m1, m2) == False
    m1 = [[1], [2], [3]]
    m2 = [[1, 2, 3]]
    assert sao_multiplicaveis(m1, m2) == True
