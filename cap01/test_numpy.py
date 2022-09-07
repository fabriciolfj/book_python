import numpy

a = numpy.arange(12)
a.shape = 3, 4 #gerar uma matriz com 3 linhas e 4 colunas
print(a)


print(a[2, 1])
a *= 5 # multiplica toda a matriz
print(a)