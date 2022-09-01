fruits= ['grape', 'rasberry', 'apple', 'banana']
print(sorted(fruits)) #ordena e gera uma nova lista, no entanto não muda a original
print(sorted(fruits, key=len, reverse=True)) #ordena pelo tamanho das palavras

fruits.sort() #ordena a muda a lista original
print(fruits)