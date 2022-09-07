nome = input("Digite seu nome: ")

if len(nome) <= 4:
    print("nome pequeno")
elif 5 <= len(nome) <= 6:
    print("normal")
else:
    print("grande")