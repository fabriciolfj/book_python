numero = input("Digite um numero inteiro: ")

if numero.isdigit():
    numero = int(numero)

    if numero % 2 == 0:
        print("Número e par")
    else:
        print("Numero e impar")
else:
    print("Não e um numero inteiro")
