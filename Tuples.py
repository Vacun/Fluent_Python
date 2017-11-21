# “Example 2-7. Tuples used as records.”

lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passports in traveler_ids:
    print('%s/%s' % passports)

for passports in sorted(traveler_ids):
    print(passports)

for passports in sorted(traveler_ids):
    print('country - {0} ** passport number - {1}'.format(*passports))

# here i can manipulate the position of the unpacked data
for passports in sorted(traveler_ids):
    print('country - {1} ** passport number - {0}'.format(*passports))


#  Unpacking and formating tuples as records: Nested tuple unpacking

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -146.635833)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:  #
        print(fmt.format(name, latitude, longitude))


# Named Tuples
from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')

tokyo = City('Tokyo', 'JP', 33.933, (35.689722, 139.691667))
