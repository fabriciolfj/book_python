from datetime import date

nome = "Fabricio Jacob"
idade = 37
altura = 1.90
peso = 120
e_maior = idade > 18
imc = peso / (altura * altura)
data_atual = date.today().year
ano_nascimento = data_atual - idade

print('{0} nasceu {1} de idade e seu imc e {2:.2f}'.format(nome, ano_nascimento, imc))
