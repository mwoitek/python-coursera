import math

def main():
    A = float(input("Digite o coeficiente A: "))
    B = float(input("Digite o coeficiente B: "))
    C = float(input("Digite o coeficiente C: "))
    Delta = B ** 2 - 4.0 * A * C
    if (Delta < 0.0):
        print("esta equação não possui raízes reais")
    elif (Delta == 0.0):
        x = (- B) / (2.0 * A)
        print("a raiz desta equação é", x)
    else:
        x1 = (- B + math.sqrt(Delta)) / (2.0 * A)
        x2 = (- B - math.sqrt(Delta)) / (2.0 * A)
        if (x1 < x2):
            print("as raízes da equação são", x1, "e", x2)
        else:
            print("as raízes da equação são", x2, "e", x1)

main()
