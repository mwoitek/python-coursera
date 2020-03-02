from lista_ordenada import *

def test_lista_ordenada():
    assert ordenada([1, 2, 3, 4]) == True
    assert ordenada([1, 2, 3, 4, 0, 7]) == False
    assert ordenada([1, 3, 5, 7, 9]) == True
    assert ordenada([5, 6, 7, 2, 9]) == False
