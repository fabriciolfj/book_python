metro_areas = [
    ('sao paulo', 'BR', (23.00, 8999.00))]
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'

for estado, _, (longitude, latitude) in metro_areas:
    print(fmt.format(estado, longitude, latitude))
