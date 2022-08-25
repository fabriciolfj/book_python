#nao gera uma lista, gera um registro por vez e nao ficam na memoria
cores = ['preto', 'branca']
tamanhos = ['GG', 'G', 'M']

for resultado in ('%s %s' % (cor, tamanho) for cor in cores for tamanho in tamanhos):
    print(resultado)