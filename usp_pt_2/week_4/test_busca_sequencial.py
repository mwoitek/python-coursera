from busca_sequencial import *

def test_busca_sequencial():
    assert busca([1, 2, 3, 4, 5], 3) == 2
    assert busca([0, 2, 4, 6, 8], 9) == False
    assert busca([0, 3, 4, 6, 8, 10], 8) == 4
    assert busca([3, 5, 7, 9, 11, 1], 6) == False
    assert busca([-3, -2, -1, 0, 1, 2, 3], 0) == 3
