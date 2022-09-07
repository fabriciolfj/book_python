idade = 37
renda = 20.000
nome = 'fabricio'

if idade > 18 and renda < 10.000:
    print("{} classe baixa".format(nome))
elif idade > 30 and renda > 10.000:
    print("{} classe media".format(nome))
else:
    print('{} classe alta'.format(nome))
