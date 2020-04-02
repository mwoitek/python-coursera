def main():
    numero = int(input("Digite um número inteiro: "))
    if (numero % 5 == 0):
        saida = "Buzz"
    else:
        saida = str(numero)
    print(saida)

main()
