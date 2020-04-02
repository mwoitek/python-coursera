from soma_matriz import *

def test_soma_matrizes():
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[2, 3, 4], [5, 6, 7]]
    assert soma_matrizes(m1, m2) == [[3, 5, 7], [9, 11, 13]]
    m1 = [[1], [2], [3]]
    m2 = [[2, 3, 4], [5, 6, 7]]
    assert soma_matrizes(m1, m2) == False
