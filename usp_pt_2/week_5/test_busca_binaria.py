from busca_binaria import *

def test_busca_binaria():
    assert busca(["a", "e", "i"], "e") == 1
    assert busca([1, 2, 3, 4, 5], 6) == False
    assert busca([1, 2, 3, 4, 5, 6], 4) == 3
