from collections import namedtuple

City = namedtuple('City', 'name country coordinates')
Coordenadas = namedtuple('Coordenadas', 'latitude longitude')
serrana = City('Serrana', 'BR', Coordenadas(299, 999))

print(serrana)
print(serrana.country)
print(serrana.coordinates)

print(City._fields)

#instanciar uma dupla a partir de uma variavel.
cidade = ('Ribeirao preto', 'br', (99, 888))
rp = City._make(cidade)

print(rp._asdict())

for key, value in rp._asdict().items():
    print(key + ':', value)