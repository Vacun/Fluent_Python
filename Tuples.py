# “Example 2-7. Tuples used as records.”

lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),('ESP', 'XDA205856')]

for passports in traveler_ids:
    print('%s/%s' % passports)

for passports in sorted(traveler_ids):
    print(passports)

for passports in sorted(traveler_ids):
    print('country - {0} ** passport number - {1}'.format(*passports))

# here i can manipulate the position of the unpacked data
for passports in sorted(traveler_ids):
    print('country - {1} ** passport number - {0}'.format(*passports))


