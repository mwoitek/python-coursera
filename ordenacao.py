def main():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    n3 = int(input("Digite o terceiro número: "))
    teste1 = n1 <= n2
    teste2 = n2 <= n3
    if (teste1 and teste2):
        saida = "crescente"
    else:
        saida = "não está em ordem crescente"
    print(saida)

main()
