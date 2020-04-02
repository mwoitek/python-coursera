from classe_triangulo import *

def test_classe_triangulo():
    tri = Triangulo(3, 4, 5)
    assert tri.a == 3
    assert tri.b == 4
    assert tri.c == 5
    assert tri.perimetro() == 12
