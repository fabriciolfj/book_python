list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(list[:2])
print(list[3:])

print(list[::3]) #vai pulando 3 em 3

print(list[2::4])

invoice = """
190990fabricio lucas jacob17.90
8892  suzana               9.00  
"""

codigo = slice(0, 6)
nome = slice(6, 26)
preco = slice(26, 31)

items = invoice.split('\n')

for item in items:
    print(item[codigo], item[nome], item[preco])