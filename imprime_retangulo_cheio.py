def main():
    largura = int(input("digite a largura: "))
    altura = int(input("digite a altura: "))
    linha = ""
    for i in range(largura):
        linha += "#"
    for i in range(altura):
        print(linha)

main()
