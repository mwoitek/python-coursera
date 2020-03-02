from tipo_triangulo import *

def test_tipo_triangulo():
    tri = Triangulo(3, 4, 5)
    assert tri.a == 3
    assert tri.b == 4
    assert tri.c == 5
    assert tri.perimetro() == 12
    assert tri.tipo_lado() == "escaleno"
    tri = Triangulo(5, 5, 6)
    assert tri.a == 5
    assert tri.b == 5
    assert tri.c == 6
    assert tri.perimetro() == 16
    assert tri.tipo_lado() == "isósceles"
    tri = Triangulo(6, 6, 6)
    assert tri.a == 6
    assert tri.b == 6
    assert tri.c == 6
    assert tri.perimetro() == 18
    assert tri.tipo_lado() == "equilátero"
