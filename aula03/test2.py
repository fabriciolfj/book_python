hora = input("Digite a hora: ")

try:
    hora = int(hora)

    if 0 <= hora <= 11:
        print("bom dia")
    elif 11 < hora <= 17:
        print("boa tarde")
    else:
        print("boa noite")
except:
    print("Hora invalida")