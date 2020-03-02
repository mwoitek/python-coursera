class Triangulo:

    def __init__(self, lado1, lado2, lado3):
        self.a = lado1
        self.b = lado2
        self.c = lado3

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        teste1 = self.a == self.b
        teste2 = self.a == self.c
        teste3 = self.b == self.c
        if teste1 and teste2 and teste3:
            return "equilátero"
        elif (not teste1) and (not teste2) and (not teste3):
            return "escaleno"
        else:
            return "isósceles"
