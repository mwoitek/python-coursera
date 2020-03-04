from soma_lista_recursivo import *

def test_soma_lista():
    assert soma_lista([1, 2, 3, 4]) == 10
    assert soma_lista([-1, 0, 1, 2]) == 2
    assert soma_lista([5, 6, 7]) == 18
    assert soma_lista([-3, -2, -1]) == -6
    assert soma_lista([4, 4, 4, 4]) == 16
    assert soma_lista([5]) == 5
    assert soma_lista([]) == 0
