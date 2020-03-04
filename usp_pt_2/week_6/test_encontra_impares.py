from encontra_impares import *

def test_encontra_impares():
    assert encontra_impares([1, 3, 5]) == [1, 3, 5]
    assert encontra_impares([2, 4, 6]) == []
    assert encontra_impares([1, 2, 3, 4, 5]) == [1, 3, 5]
    assert encontra_impares([2, 4, 6, 7]) == [7]
    assert encontra_impares([]) == []
    assert encontra_impares([1, 1, 1, 2]) == [1, 1, 1]
