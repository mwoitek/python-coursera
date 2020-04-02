def main():
    numero = int(input("Digite um número inteiro: "))
    if (numero % 3 == 0):
        saida = "Fizz"
    else:
        saida = str(numero)
    print(saida)

main()
