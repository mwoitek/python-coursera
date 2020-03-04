import math

def main():
    x1 = float(input("Digite a primeira coordenada x: "))
    y1 = float(input("Digite a primeira coordenada y: "))
    x2 = float(input("Digite a segunda coordenada x: "))
    y2 = float(input("Digite a segunda coordenada y: "))
    temp = (x1 - x2) ** 2 + (y1 - y2) ** 2
    dist = math.sqrt(temp)
    if (dist >= 10.0):
        saida = "longe"
    else:
        saida = "perto"
    print(saida)

main()
