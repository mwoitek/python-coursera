def main():
    numero = int(input("Digite um número inteiro: "))
    div3 = numero % 3 == 0
    div5 = numero % 5 == 0
    if (div3 and div5):
        saida = "FizzBuzz"
    else:
        saida = str(numero)
    print(saida)

main()
