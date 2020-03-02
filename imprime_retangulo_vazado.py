def main():
    largura = int(input("digite a largura: "))
    altura = int(input("digite a altura: "))
    linha1 = ""
    for i in range(largura):
        linha1 += "#"
    linha2 = "#"
    for i in range(largura - 2):
        linha2 += " "
    linha2 += "#"
    print(linha1)
    for i in range(altura - 2):
        print(linha2)
    print(linha1)

main()
