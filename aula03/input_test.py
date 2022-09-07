from datetime import date

nome  = input("Qual seu nome? ")
idade = input("Qual sua idade? ")

ano_nascimento = date.today().year - int(idade)

print()
print("{0} nasceu no ano {1}.".format(nome, ano_nascimento))