def main():
    L = int(input("Digite o valor correspondente ao lado de um quadrado: "))
    perimetro = 4 * L
    area = L ** 2
    saida = "perímetro: {:d} - área: {:d}"
    print(saida.format(perimetro, area))

main()
