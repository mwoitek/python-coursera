def main():
    n = int(input("Digite o valor de n: "))
    if (n == 0):
        saida = "1"
    else:
        fatorial = 1
        k = 2
        while (k <= n):
            fatorial *= k
            k += 1
        saida = str(fatorial)
    print(saida)

main()
