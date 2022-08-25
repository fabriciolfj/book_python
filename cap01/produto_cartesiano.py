colors = ['preto', 'branca']
tamanhos = ['GG', 'G', 'M']

#para gerar listas em memoria, utiliza-se o listacomps (list comprehensions)
resultado = [(cor, tamanho) for cor in colors for tamanho in tamanhos]
print(resultado)