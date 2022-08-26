lax_coordinates = (33.94, -118.40)
city, year, pop, chg, are = ('tokyo', 2003, 32450, 0.66, 8014)

traveler_ids = [('USA', '31195855'), ('BRA', 'CE34267'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

#segundo valor é atributo ao _, usamos essa tecnica quando nao queremos utilizar o valor
for country, _ in traveler_ids:
    print(country)

latitude, longitude = lax_coordinates
print(latitude)
print(longitude)

print(divmod(10, 5))

t = (10, 5)
print(divmod(*t))

